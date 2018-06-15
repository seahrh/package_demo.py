# Use Packages to Organise Modules and Export APIs

## TL;DR

`__all__` is probably not worth it because Python does not enforce private packages.
So subpackages can always be imported, breaking encapsulation.

Consider `__all__` if you do not need subpackages, and rely only on modules to organise your code.

## What are packages?

In Python, packages are modules that contain other modules.

## Why export APIs?

Key benefit: Encapsulation

To provide public parts of the API as a set of attributes that are
**available on the top-level package**.
This will allow API users to import directly from the top-level package instead of the subpackage.
This ensures that users' code will continue to work
even if the internal organization of the API changes.

## How to export API

Hence, to determine the public interface of the API, `__all__` should be explicitly defined in all modules. 

Given the following project structure:
```
package1_user.py
package1/__init__.py
package1/module1.py
package1/module2.py
package1/package2/__init__.py
package1/package2/module3.py
package1/package2/module4.py
```

`package1` is the top-level package of the exported API.

Goal: Export a function that is defined in a module

Set `__all__` in the module
```python
# module2.py
__all__ = ['bar_module2']

def bar_module2():
    ...
```

Set `__all__` in the top-level package of the API. 
```python
# package1/__init__.py
from . module1 import *
from . module2 import *
from . package2 import *
__all__ = []
__all__ += module1.__all__
__all__ += module2.__all__
__all__ += package2.__all__
```

User can import the function directly from `package1` even though it is defined in `module2`.
```python
from package1 import bar_module2
```

The same applies to subpackages. Function `bar_module4` is defined in `package2`.
```python
from package1 import bar_module4
```

Note, however, that functions defined in `__init__.py` are always exported even if they are not included in the `__all__` attribute.
```python
from package1 import bar_package1
```

Subpackages can always be imported though, so it is a leaky abstraction.
Perhaps when exporting an API, prefer a flat structure without subpackages.  
```python
from package1.package2 import _foo_package2 # Leaky!
```

For more examples, see [package1_user.py](package1_user.py)

## Notes

Tested on Python 3.6.5.

## References

1. Effective Python, Brett Slatkin, Item 50: Use Packages to Organize Modules and Provide
Stable APIs
2. python.org - The Python Tutorial: [Modules](https://docs.python.org/3/tutorial/modules.html)
3. PEP8 - [Public and Internal Interfaces](https://www.python.org/dev/peps/pep-0008/#public-and-internal-interfaces)

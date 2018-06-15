from package1 import *
from package1 import package2, _package3

# Following imports work but trigger a warning:
# class/function is not declared in __all__
# from package1.module1 import NonExportedClassModule1
# from package1.module2 import _foo_module2

m1 = ExportedClassModule1()
bar_module2()
bar_package2()

# This call requires package prefix
# because function is not included in __all__

package2.tin_package2()
package2._foo_package2()
_package3._foo_package3()

# Following is not exported in API
# c = NonExportedClassModule1()
# _foo_module2()

import package1
__dir = dir(package1)
print(f'dir(package1)={repr(__dir)}')
assert __dir == [
    'ExportedClassModule1',
    'ExportedClassModule3',
    '__all__',
    '__builtins__',
    '__cached__',
    '__doc__',
    '__file__',
    '__loader__',
    '__name__',
    '__package__',
    '__path__',
    '__spec__',
    '_foo_package1',
    '_package3',
    'bar_module2',
    'bar_module4',
    'bar_package1',
    'bar_package2',
    'module1',
    'module2',
    'package2'
]
__dir = dir(package2)
print(f'dir(package2)={repr(__dir)}')
assert __dir == [
    'ExportedClassModule3',
    '__all__',
    '__builtins__',
    '__cached__',
    '__doc__',
    '__file__',
    '__loader__',
    '__name__',
    '__package__',
    '__path__',
    '__spec__',
    '_foo_package2',
    'bar_module4',
    'bar_package2',
    'module3',
    'module4',
    'tin_package2'
]
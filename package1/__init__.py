from . module1 import *
from . module2 import *
from . package2 import *
__all__ = []
__all__ += module1.__all__
__all__ += module2.__all__
__all__ += package2.__all__


def bar_package1():
    """This will always be exposed even if it is not included in `__all__`.
    """
    pass


def _foo_package1():
    """This will always be exposed even if it is not included in `__all__`.
    The name having one or two leading underscores does not matter.
    """
    pass

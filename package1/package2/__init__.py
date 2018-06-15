from . module3 import *
from . module4 import *
__all__ = ['bar_package2']
__all__ += module3.__all__
__all__ += module4.__all__


def bar_package2():
    """This will always be exposed even if it is not included in `__all__`.
    """
    pass


def tin_package2():
    """This will always be exposed even if it is not included in `__all__`.
    """
    pass


def _foo_package2():
    """This will always be exposed even if it is not included in `__all__`.
    The name having one or two leading underscores does not matter.
    """
    pass

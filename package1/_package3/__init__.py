__all__ = []


def bar_package3():
    """This will always be exposed even if it is not included in `__all__`.
    """
    pass


def tin_package3():
    """This will always be exposed even if it is not included in `__all__`.
    """
    pass


def _foo_package3():
    """This will always be exposed even if it is not included in `__all__`.
    The name having one or two leading underscores does not matter.
    """
    pass

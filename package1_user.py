from package1 import *

# Following imports work but trigger a warning:
# class/function is not declared in __all__
# from package1.module1 import NonExportedClass
# from package1.module2 import _foo_module2

a = Projectile(1.5, 3)
b = Projectile(4, 1.7)
bar_module2()

# Following is not exported in API
# c = NonExportedClass()
# _foo_module2()


import package1
__dir = dir(package1)
print(f'dir(package1)={repr(__dir)}')
assert __dir == [
    'Projectile',
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
    'bar_module2',
    'bar_package1',
    'module1',
    'module2'
]

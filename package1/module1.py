__all__ = ['Projectile']


class Projectile(object):
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity


class NonExportedClass(object):
    def __init__(self):
        pass

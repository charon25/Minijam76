from _atom_ import NeutronAtom, FissileAtom


class U234(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.texture = None


class U235(FissileAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.texture = None


class U236(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.texture = None


class U238(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.texture = None


class Pu239(FissileAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.texture = None
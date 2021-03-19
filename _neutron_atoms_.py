from _atoms_ import NeutronAtom, FissileAtom
import _texture_manager_ as Textures
import co


class U234(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.U234_SIZE, co.U234_SIZE)
        self.texture = Textures.U234_TEXTURE.convert_alpha()


class U235(FissileAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.U235_SIZE, co.U235_SIZE)
        self.texture = Textures.U235_TEXTURE.convert_alpha()


class U236(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.U236_SIZE, co.U236_SIZE)
        self.texture = Textures.U236_TEXTURE.convert_alpha()


class U238(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.U238_SIZE, co.U238_SIZE)
        self.texture = Textures.U238_TEXTURE.convert_alpha()


class Pu239(FissileAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.PU239_SIZE, co.PU239_SIZE)
        self.texture = Textures.PU239_TEXTURE.convert_alpha()
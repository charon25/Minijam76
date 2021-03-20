import _texture_manager_ as textures
import _atoms_ as atoms
import co
  

class Kr93(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.KR93_SIZE, co.KR93_SIZE, vx, vy)
        self.texture = textures.KR93_TEXTURE.convert_alpha()
        
        
class Sr94(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.SR94_SIZE, co.SR94_SIZE, vx, vy)
        self.texture = textures.SR94_TEXTURE.convert_alpha()
        

class Zr103(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.ZR103_SIZE, co.ZR103_SIZE, vx, vy)
        self.texture = textures.ZR103_TEXTURE.convert_alpha()
        

class Xe134(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.XE134_SIZE, co.XE134_SIZE, vx, vy)
        self.texture = textures.XE134_TEXTURE.convert_alpha()
        
        
class Xe140(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.XE140_SIZE, co.XE140_SIZE, vx, vy)
        self.texture = textures.XE140_TEXTURE.convert_alpha()
        
        
class Ba140(atoms.Atom):
    def __init__(self, x, y, vx=0.0, vy=0.0):
        super().__init__(x, y, co.BA140_SIZE, co.BA140_SIZE, vx, vy)
        self.texture = textures.BA140_TEXTURE.convert_alpha()
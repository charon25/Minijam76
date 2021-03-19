from _atoms_ import Atom  
import _texture_manager_ as Textures
import co
  

class Kr93(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.KR93_SIZE, co.KR93_SIZE)
        self.texture = Textures.KR93_TEXTURE.convert_alpha()
        
        
class Sr94(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.SR94_SIZE, co.SR94_SIZE)
        self.texture = Textures.SR94_TEXTURE.convert_alpha()
        

class Zr103(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.ZR103_SIZE, co.ZR103_SIZE)
        self.texture = Textures.ZR103_TEXTURE.convert_alpha()
        

class Xe134(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.XE134_SIZE, co.XE134_SIZE)
        self.texture = Textures.XE134_TEXTURE.convert_alpha()
        
        
class Xe140(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.XE140_PATH, co.XE140_SIZE)
        self.texture = Textures.XE140_TEXTURE.convert_alpha()
        
        
class Ba140(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, co.BA140_SIZE, co.BA140_SIZE)
        self.texture = Textures.BA140_TEXTURE.convert_alpha()
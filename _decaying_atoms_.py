from _atoms_ import DecayingAtom
import _texture_manager_ as Textures
import co


class U237(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.U237_SIZE, co.U237_SIZE, decay_time)
        self.texture = Textures.U238_TEXTURE.convert_alpha()
        
class U239(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.U239_SIZE, co.U239_SIZE, decay_time)
        self.texture = Textures.U239_TEXTURE.convert_alpha()
        
        
class Np237(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.NP237_SIZE, co.NP237_SIZE, decay_time)
        self.texture = Textures.NP237_TEXTURE.convert_alpha()
        
        
class Np238(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.NP238_SIZE, co.NP238_SIZE, decay_time)
        self.texture = Textures.NP238_TEXTURE.convert_alpha()
        
        
class Np239(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.NP239_SIZE, co.NP239_SIZE, decay_time)
        self.texture = Textures.NP239_TEXTURE.convert_alpha()
        
        
class Pu238(DecayingAtom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, co.PU238_SIZE, co.PU238_SIZE, decay_time)
        self.texture = Textures.PU238_TEXTURE.convert_alpha()
        
        
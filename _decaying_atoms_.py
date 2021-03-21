import pygame as pyg
import _texture_manager_ as textures
import _atoms_ as atoms
import _neutron_atoms_ as neutron_atoms
import _texture_manager_ as textures
import co


class U237(atoms.DecayingAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.U237_SIZE, co.U237_SIZE, co.U237_DECAY)
        self.texture = textures.U237_TEXTURE.convert_alpha()
        
    def disintegrate(self):
        pyg.event.post(pyg.event.Event(co.DISINTEGRATION_TYPE))
        self.to_delete = True
        self.created_atoms.append(neutron_atoms.Np237(self.x0, self.y0))
        
        
class U239(atoms.DecayingAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.U239_SIZE, co.U239_SIZE, co.U239_DECAY)
        self.texture = textures.U239_TEXTURE.convert_alpha()
        
    def disintegrate(self):
        pyg.event.post(pyg.event.Event(co.DISINTEGRATION_TYPE))
        self.to_delete = True
        self.created_atoms.append(Np239(self.x0, self.y0))
       
        
class Np238(atoms.DecayingAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.NP238_SIZE, co.NP238_SIZE, co.NP238_DECAY)
        self.texture = textures.NP238_TEXTURE.convert_alpha()
        
    def disintegrate(self):
        pyg.event.post(pyg.event.Event(co.DISINTEGRATION_TYPE))
        self.to_delete = True
        self.created_atoms.append(Pu238(self.x0, self.y0))
        
        
class Np239(atoms.DecayingAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.NP239_SIZE, co.NP239_SIZE, co.NP239_DECAY)
        self.texture = textures.NP239_TEXTURE.convert_alpha()
        
    def disintegrate(self):
        pyg.event.post(pyg.event.Event(co.DISINTEGRATION_TYPE))
        self.to_delete = True
        self.created_atoms.append(neutron_atoms.Pu239(self.x0, self.y0))
        
        
class Pu238(atoms.DecayingAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.PU238_SIZE, co.PU238_SIZE, co.PU239_DECAY)
        self.texture = textures.PU238_TEXTURE.convert_alpha()
        
    def disintegrate(self):
        pyg.event.post(pyg.event.Event(co.DISINTEGRATION_TYPE))
        self.to_delete = True
        self.created_atoms.append(neutron_atoms.U234(self.x0, self.y0, 2))
        
        
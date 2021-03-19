import co


class Atom():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.texture = None
        self.can_decay = False
        self.can_absorb_neutron = False
        
        
    def show(self):
        pass
        
class DecayingAtom(Atom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, h, w)
        self.can_decay = True
        self.decay_time = decay_time
        
        
    def age(self):
        pass
    
class NeutronAtom(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.can_absorb_neutron = True
    
class FissileAtom(NeutronAtom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        
        
    def fission(self, neutrons_count):
        pass

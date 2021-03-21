import co
import random, math
import util
import _neutrons_ as neutrons
import _electrons_ as electrons
import pygame as pyg

class Atom():
    def __init__(self, x, y, w, h, vx=0.0, vy=0.0):
        self.x = float(x)
        self.y = float(y)
        self.w = w
        self.h = h
        self.vx = float(vx)
        self.vy = float(vy)
        self.texture = None
        #States
        self.can_decay = False
        self.can_absorb_neutron = False
        #Objects
        self.to_delete = False
        self.created_atoms = []
        self.created_neutrons = []
        self.electron = None
        #Value
        self.over = 0
        
    def reset(self):
        #Objects
        self.to_delete = False
        self.created_atoms = []
        self.created_neutrons = []
        self.electron = None
        #Value
        self.over = 0
        
        
    def get_position(self):
        return (self.x, self.y)
    
    def move(self, r):
        self.x += self.vx * r
        self.y += self.vy * r
        
        if self.x < 0 or self.x + self.w > co.WIDTH:
            self.reflect_vertical()
        if self.y < 0 or self.y + self.h > co.HEIGHT:
            self.reflect_horizontal()
        
        if self.vx > 0:
            self.vx = max(0, self.vx - co.ATOM_BRAKE * r)
        elif self.vx < 0:
            self.vx = min(0, self.vx + co.ATOM_BRAKE * r)
        if self.vy > 0:
            self.vy = max(0, self.vy - co.ATOM_BRAKE * r)
        elif self.vy < 0:
            self.vy = min(0, self.vy + co.ATOM_BRAKE * r)
            
    def reflect_horizontal(self):
        self.vy *= -1
        
    def reflect_vertical(self):
        self.vx *= -1
        
    def has_created_atoms(self):
        return (len(self.created_atoms) > 0)
        
    def has_created_neutrons(self):
        return (len(self.created_neutrons) > 0)
    
    def has_emitted_electron(self):
        return (self.electron is not None)
        
    def age(self, dt):
        pass
    
    def is_hit_by_neutron(self, neutron):
        pass
    
        
class DecayingAtom(Atom):
    def __init__(self, x, y, w, h, decay_time):
        super().__init__(x, y, h, w)
        self.x0 = x
        self.y0 = y
        self.can_decay = True
        self.decay_time = decay_time
        self.initial_decay_time = decay_time
        self.over = 1
        
    def reset(self):
        self.to_delete = False
        self.created_atoms = []
        self.created_neutrons = []
        self.electron = None
        self.over = 1
        self.decay_time = self.initial_decay_time
        
    def age(self, dt):
        self.decay_time -= dt
        max_shake = int(co.DECAY_MAX_SHAKE * (1 - self.decay_time / self.initial_decay_time))
        self.x = self.x0 + random.randint(-max_shake, max_shake)
        self.y = self.y0 + random.randint(-max_shake, max_shake)
        if self.decay_time <= 0:
            self.emit_electron()
            self.disintegrate()
            
    def disintegrate(self):
        pass
    
    def emit_electron(self):
        vx, vy = util.polar_to_cartesian(co.ELECTRON_SPEED, random.uniform(0, 2*math.pi))
        self.electron = electrons.Electron(self.x0 + self.w / 2, self.y0 + self.h / 2, vx, vy)
        
    
class NeutronAtom(Atom):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.can_absorb_neutron = True
        self.over = 1     
        
    def reset(self):
        self.to_delete = False
        self.created_atoms = []
        self.created_neutrons = []
        self.electron = None
        self.over = 1
        
    def is_hit_by_neutron(self, neutron):
        pass

import _atoms_ as atoms
import _stable_atoms_ as stable_atoms
import _decaying_atoms_ as decaying_atoms
import _texture_manager_ as textures
import _neutrons_ as neutrons
import co
import util
import random

class U234(atoms.NeutronAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.U234_SIZE, co.U234_SIZE)
        self.texture = textures.U234_TEXTURE.convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        self.created_atoms.append(U235(self.x, self.y))


class U235(atoms.NeutronAtom):
    def __init__(self, x, y, _type):
        super().__init__(x, y, co.U235_SIZE, co.U235_SIZE)
        self.type = _type
        self.texture = textures.U235_TEXTURES[self.type].convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        if self.type == co.U235_NEUTRON:
            self.created_atoms.append(U236(self.x, self.y))
        elif self.type == co.U235_SRXE2:
            self.create_sr_xe(neutron)
        elif self.type == co.U235_KRBA3:
            self.created_kr_ba(neutron)
            
            
    def create_sr_xe(self, neutron):
        cx = self.x + self.w / 2
        cy = self.y + self.h / 2
        #Neutrons
        neut1 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, co.NEUTRON_CREATION_ANGLE_U))
        neut2 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, -co.NEUTRON_CREATION_ANGLE_U))
        self.created_neutrons += [neut1, neut2]
        #Atomes
        sr = stable_atoms.Sr94(cx - co.SR94_SIZE / 2,
                               cy - co.SR94_SIZE / 2,
                               *util.vector_rotation(neutron.vx,
                                                     neutron.vy,
                                                     random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                     co.ATOM_CREATION_SPEED_FACTOR))
        xe = stable_atoms.Xe140(cx - co.XE140_SIZE / 2,
                                cy - co.XE140_SIZE / 2,
                                *util.vector_rotation(neutron.vx,
                                                      neutron.vy,
                                                      -random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                      co.ATOM_CREATION_SPEED_FACTOR))
        self.created_atoms += [sr, xe]
        
    def created_kr_ba(self, neutron):
        cx = self.x + self.w / 2
        cy = self.y + self.h / 2
        #Neutrons
        neut1 = neutrons.Neutron(cx, cy, neutron.vx, neutron.vy)
        neut2 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, co.NEUTRON_CREATION_ANGLE_U))
        neut3 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, -co.NEUTRON_CREATION_ANGLE_U))
        self.created_neutrons += [neut1, neut2, neut3]
        #Atomes
        kr = stable_atoms.Kr93(cx - co.KR93_SIZE / 2,
                               cy - co.KR93_SIZE / 2,
                               *util.vector_rotation(neutron.vx,
                                                     neutron.vy,
                                                     random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                     co.ATOM_CREATION_SPEED_FACTOR))
        ba = stable_atoms.Ba140(cx - co.BA140_SIZE / 2,
                                cy - co.BA140_SIZE / 2,
                                *util.vector_rotation(neutron.vx,
                                                     neutron.vy,
                                                     -random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                     co.ATOM_CREATION_SPEED_FACTOR))
        self.created_atoms += [kr, ba]
        

class U236(atoms.NeutronAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.U236_SIZE, co.U236_SIZE)
        self.texture = textures.U236_TEXTURE.convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        self.created_atoms.append(decaying_atoms.U237(self.x, self.y))


class U238(atoms.NeutronAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.U238_SIZE, co.U238_SIZE)
        self.texture = textures.U238_TEXTURE.convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        self.created_atoms.append(decaying_atoms.U239(self.x, self.y))
        

class Np237(atoms.NeutronAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.NP237_SIZE, co.NP237_SIZE)
        self.texture = textures.NP237_TEXTURE.convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        self.created_atoms.append(decaying_atoms.Np238(self.x, self.y))


class Pu239(atoms.NeutronAtom):
    def __init__(self, x, y):
        super().__init__(x, y, co.PU239_SIZE, co.PU239_SIZE)
        self.texture = textures.PU239_TEXTURE.convert_alpha()
        
    def is_hit_by_neutron(self, neutron):
        self.to_delete = True
        neutron.to_delete = True
        cx = self.x + self.w / 2
        cy = self.y + self.h / 2
        #Neutrons
        neut1 = neutrons.Neutron(cx, cy, neutron.vx, neutron.vy)
        neut2 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, co.NEUTRON_CREATION_ANGLE_PU))
        neut3 = neutrons.Neutron(cx, cy, *util.vector_rotation(neutron.vx, neutron.vy, -co.NEUTRON_CREATION_ANGLE_PU))
        self.created_neutrons += [neut1, neut2, neut3]
        #Atomes
        zr = stable_atoms.Zr103(cx - co.ZR103_SIZE / 2,
                                cy - co.ZR103_SIZE / 2,
                                *util.vector_rotation(neutron.vx,
                                                      neutron.vy,
                                                      random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                      co.ATOM_CREATION_SPEED_FACTOR))
        xe = stable_atoms.Xe134(cx - co.XE134_SIZE / 2,
                                cy - co.XE134_SIZE / 2,
                                *util.vector_rotation(neutron.vx,
                                                      neutron.vy,
                                                      -random.randint(co.ATOM_CREATION_ANGLE_MIN, co.ATOM_CREATION_ANGLE_MAX),
                                                      co.ATOM_CREATION_SPEED_FACTOR))
        self.created_atoms += [zr, xe]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
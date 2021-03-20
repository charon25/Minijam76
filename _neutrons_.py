import co
import _texture_manager_ as Textures

class Neutron():
    def __init__(self, x, y, vx=0.0, vy=0.0):
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.texture = Textures.NEUTRON_TEXTURE.convert_alpha()
        
    def move(self, r):
        self.x += self.vx * r
        self.y += self.vy * r
        #Réflection contre les murs
        if self.x < 0 or self.x + co.NEUTRON_SIZE > co.WIDTH:
            self.reflect_vertical()
        if self.y < 0 or self.y + co.NEUTRON_SIZE > co.HEIGHT:
            self.reflect_horizontal()
            
    def get_position(self):
        return (self.x, self.y)
        
    def reflect_horizontal(self):
        self.vy *= -1
        
    def reflect_vertical(self):
        self.vx *= -1
        
    def does_collide_with_atom(self, atom):
        if not atom.can_absorb_neutron:
            return False
        if self.x + co.NEUTRON_SIZE < atom.x:
            return False
        if self.x > atom.x + atom.w:
            return False
        if self.y + co.NEUTRON_SIZE < atom.y:
            return False
        if self.y > atom.y + atom.h:
            return False
        return True
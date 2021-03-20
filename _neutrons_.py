import co
import _texture_manager_ as Textures

class Neutron():
    def __init__(self, x, y, vx=0.0, vy=0.0):
        self.x = float(x - co.NEUTRON_SIZE / 2)
        self.y = float(y - co.NEUTRON_SIZE / 2)
        self.vx = float(vx)
        self.vy = float(vy)
        self.texture = Textures.NEUTRON_TEXTURE.convert_alpha()
        self.bounces = 0
        self.to_delete = False
        self.last_wall_x = -1
        self.last_wall_y = -1
        
    def move(self, r):
        self.x += self.vx * r
        self.y += self.vy * r
        #Réflection contre les murs
        if self.x < 0:
            self.reflect_vertical(0)
        elif self.x + co.NEUTRON_SIZE > co.WIDTH:
            self.reflect_vertical(1)
        if self.y < 0:
            self.reflect_horizontal(0)
        elif self.y + co.NEUTRON_SIZE > co.HEIGHT:
            self.reflect_horizontal(1)
            
    def get_position(self):
        return (self.x, self.y)
        
    def reflect_horizontal(self, side):
        if self.last_wall_y == side:
            return
        self.last_wall_y = side
        self.add_bounce()
        self.vy *= -1
        
    def reflect_vertical(self, side):
        if self.last_wall_x == side:
            return
        self.last_wall_x = side
        self.add_bounce()
        self.vx *= -1
        
    def add_bounce(self):
        self.bounces += 1
        if self.bounces > co.NEUTRON_MAX_BOUNCES:
            self.to_delete = True
        
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
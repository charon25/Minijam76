import co
import _texture_manager_ as textures

class Electron():
    def __init__(self, x, y, vx, vy):
        self.x = float(x - co.ELECTRON_SIZE / 2)
        self.y = float(y - co.ELECTRON_SIZE / 2)
        self.vx = float(vx)
        self.vy = float(vy)
        self.texture = textures.ELECTRON_TEXTURE.convert_alpha()
        self.to_delete = False
            
    def get_position(self):
        return (self.x, self.y)
        
    def move(self, r):
        self.x += self.vx * r
        self.y += self.vy * r
        
        if self.x < 0 or self.x + co.ELECTRON_SIZE > co.WIDTH or self.y < 0 or self.y + co.ELECTRON_SIZE > co.HEIGHT:
            self.to_delete = True
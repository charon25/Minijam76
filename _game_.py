import pygame as pyg
import co
import _events_ as events
import _atoms_ as atoms
import _stable_atoms_ as stable_atoms
import _neutron_atoms_ as neutron_atoms
import _decaying_atoms_ as decaying_atoms
import _neutrons_ as neutrons
import _texture_manager_ as textures
import util
import time, math

class Game():
    def __init__(self):
        self.is_ended = False
    
    def start(self):
        pyg.init()
        pyg.display.set_caption(co.SCREEN_TITLE)
        self.screen = pyg.display.set_mode(co.SCREEN_SIZE)
        #Listener
        self.listener = events.EventListener()
        self.listener.set_quit_callback(self.stopping)
        self.listener.set_mousedown_callback(self.mousedown)
        self.listener.set_mouseup_callback(self.mouseup)
        self.listener.set_mousemove_callback(self.mousemove)
        #Horloge
        self.clock = pyg.time.Clock()
        #Objets
        self.neutrons = []
        self.atoms = []
        self.atoms.append(stable_atoms.Kr93(700, 300))
        self.atoms.append(neutron_atoms.U234(800, 300))
        self.electrons = []
        #Actions
        self.is_clicking = False
        self.can_play = False
        self.is_far_enough = False
        self.click_x = -1
        self.click_y = -1
        self.mouse_x = -1
        self.mouse_y = -1
        
        
    def stopping(self):
        self.is_ended = True
        
    def stop(self):
        pyg.display.quit()
        pyg.quit()
    
    def loop(self):
        #if len(self.atoms) > 0:print(self.atoms[0].vx, self.atoms[0].vy)
        dt = self.clock.tick(500)
        self.listener.listen()
        self.screen.fill((255, 255, 255))
        
        for electron in self.electrons:
            electron.move(dt / co.FRAME_INTERVAL)
            self.screen.blit(electron.texture, electron.get_position())
            
        self.electrons[:] = [electron for electron in self.electrons if not electron.to_delete]
        
        for neutron in self.neutrons:
            neutron.move(dt / co.FRAME_INTERVAL)
            self.screen.blit(neutron.texture, neutron.get_position())
            for atom in self.atoms:
                if neutron.does_collide_with_atom(atom):
                    atom.is_hit_by_neutron(neutron)
                    
        self.neutrons[:] = [neutron for neutron in self.neutrons if not neutron.to_delete]
            
        for atom in self.atoms:
            atom.move(dt / co.FRAME_INTERVAL)
            atom.age(dt)
            self.screen.blit(atom.texture, atom.get_position())
            if atom.has_created_atoms():
                self.atoms += atom.created_atoms
            if atom.has_created_neutrons():
                self.neutrons += atom.created_neutrons
            if atom.has_emitted_electron():
                self.electrons.append(atom.electron)
            
        self.atoms[:] = [atom for atom in self.atoms if not atom.to_delete]
        
        self.can_play = (len(self.neutrons) == 0)
        self.is_far_enough = (util.distance(self.click_x, self.click_y, self.mouse_x, self.mouse_y) >= co.MIN_DISTANCE_TO_PLAY)
        if self.is_clicking and self.can_play:
            self.draw_player_arrow()
            
        pyg.display.flip()
        
    def mousedown(self, x, y, button):
        if button == co.LEFT_CLICK:
            self.is_clicking = True
            self.click_x = x
            self.click_y = y
        if button == co.RIGHT_CLICK:
            self.is_clicking = False
    
    def mouseup(self, x, y, button):
        if button != co.LEFT_CLICK:
            return
        if self.can_play and self.is_clicking and self.is_far_enough:
            self.generate_neutron()
        self.is_clicking = False
        self.click_x = -1
        self.click_y = -1
    
    def mousemove(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
    
    def draw_player_arrow(self):
        if self.is_far_enough:
            pyg.draw.line(self.screen, co.ARROW_COLOR_FAR, (self.click_x, self.click_y), (self.mouse_x, self.mouse_y), co.ARROW_WIDTH)
        else:
            pyg.draw.line(self.screen, co.ARROW_COLOR_CLOSE, (self.click_x, self.click_y), (self.mouse_x, self.mouse_y), co.ARROW_WIDTH)
    
    def generate_neutron(self):
        angle = math.pi/2 - math.atan2(self.mouse_x - self.click_x, (self.mouse_y - self.click_y))
        vx, vy = util.polar_to_cartesian(co.NEUTRON_SPEED, angle)
        neutron = neutrons.Neutron(self.click_x, self.click_y, vx, vy)
        self.neutrons.append(neutron)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
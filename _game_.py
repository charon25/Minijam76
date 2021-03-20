import pygame as pyg
import co
import _events_ as events
import _atoms_ as atoms
import _stable_atoms_ as stable_atoms
import _neutron_atoms_ as neutron_atoms
import _decaying_atoms_ as decaying_atoms
import _neutrons_ as neutrons
import time

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
        #Actions
        self.is_clicking = False
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
            
        self.atoms[:] = [atom for atom in self.atoms if not atom.to_delete]
        
        if self.is_clicking:
            pyg.draw.line(self.screen, (0, 0, 0), (self.click_x, self.click_y), (self.mouse_x, self.mouse_y))
            
        pyg.display.flip()
        
    def mousedown(self, x, y, button):
        if button != 1:
            return
        self.is_clicking = True
        self.click_x = x
        self.click_y = y
        pass
    
    def mouseup(self, x, y, button):
        if button != 1:
            return
        self.is_clicking = False
        self.click_x = -1
        self.click_y = -1
        pass
    
    def mousemove(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
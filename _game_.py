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
        #Horloge
        self.clock = pyg.time.Clock()
        #Objets
        self.neutrons = []
        self.atoms = []
        
        
    def stopping(self):
        self.is_ended = True
        
    def stop(self):
        pyg.display.quit()
        pyg.quit()
    
    def loop(self):
        dt = self.clock.tick(500)
        self.listener.listen()
        self.screen.fill((255, 255, 255))
        
        for neutron in self.neutrons:
            neutron.move(dt / co.FRAME_INTERVAL)
            self.screen.blit(neutron.texture, neutron.get_position())
            
        for atom in self.atoms:
            atom.move(dt / co.FRAME_INTERVAL)
            atom.age(dt)
            self.screen.blit(atom.texture, atom.get_position())
            if atom.has_created_atoms():
                self.atoms += atom.created_atoms
            if atom.has_created_neutrons():
                self.neutrons += atom.created_neutrons
            
        self.atoms[:] = [atom for atom in self.atoms if not atom.to_delete]
            
        pyg.display.flip()
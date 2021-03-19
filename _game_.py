import pygame as pyg
import co
from _events_ import EventListener
from _neutrons_ import Neutron
from _stable_atoms_ import Kr93, Sr94, Zr103, Xe134, Xe140, Ba140
from _neutron_atoms_ import U234, U235, U236, U238, Pu239
from _decaying_atoms_ import U237, U239, Np237, Np238, Np239, Pu238
import time

class Game():
    def __init__(self):
        self.is_ended = False
    
    def start(self):
        pyg.init()
        pyg.display.set_caption(co.SCREEN_TITLE)
        self.screen = pyg.display.set_mode(co.SCREEN_SIZE)
        #Listener
        self.listener = EventListener()
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
            neutron.move(dt)
            self.screen.blit(neutron.texture, neutron.get_position())
            
        for atom in self.atoms:
            self.screen.blit(atom.texture, atom.get_position())
            
        pyg.display.flip()
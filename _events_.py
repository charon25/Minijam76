import pygame as pyg

class EventListener():
    def __init__(self):
        self.quit = None
        pass
    
    def set_quit_callback(self, callback):
        self.quit = callback
    
    def listen(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.quit()
        
    

class Event():
    def __init__(self):
        pass
    

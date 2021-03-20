import pygame as pyg

class EventListener():
    def __init__(self):
        self.quit = None
        self.mousedown = None
        self.mouseup = None
        self.movemove = None
        pass
    
    def set_quit_callback(self, callback):
        self.quit = callback
        
    def set_mousedown_callback(self, callback):
        self.mousedown = callback
        
    def set_mouseup_callback(self, callback):
        self.mouseup = callback
        
    def set_mousemove_callback(self, callback):
        self.mousemove = callback
               
    
    def listen(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.quit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                self.mousedown(x=event.pos[0], y=event.pos[1], button=event.button)
            elif event.type == pyg.MOUSEBUTTONUP:
                self.mouseup(x=event.pos[0], y=event.pos[1], button=event.button)
            elif event.type == pyg.MOUSEMOTION:
                self.mousemove(x=event.pos[0], y=event.pos[1], dx=event.rel[0], dy=event.rel[1])
    

class Event():
    def __init__(self):
        pass
    

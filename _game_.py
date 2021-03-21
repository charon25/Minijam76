import pygame as pyg
import co
import _events_ as events
import _atoms_ as atoms
import _stable_atoms_ as stable_atoms
import _neutron_atoms_ as neutron_atoms
import _decaying_atoms_ as decaying_atoms
import _neutrons_ as neutrons
import _texture_manager_ as textures
import _levels_manager_ as levels_manager
import util
import time, math

class Game():
    def __init__(self):
        self.is_ended = False
    
    def start(self):
        pyg.init()
        pyg.display.set_caption(co.SCREEN_TITLE)
        self.screen = pyg.display.set_mode(co.SCREEN_SIZE)
        #Textures
        self.background = textures.BACKGROUND_TEXTURE.convert_alpha()
        self.menu = textures.MENU_TEXTURE.convert_alpha()
        #Listener
        self.listener = events.EventListener()
        self.listener.set_quit_callback(self.stopping)
        #Etat
        self.game_state = None
        self.change_state(co.MENU_STATE)
        self.levels = levels_manager.Levels()
        self.level_text = ["", ""]
        #Horloge
        self.clock = pyg.time.Clock()
        #Objets
        self.neutrons = []
        self.launched_neutron = 0
        self.atoms = []
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
        
    def change_state(self, new_state):
        self.game_state = new_state
        if self.game_state == co.MENU_STATE:
            self.listener.set_mousedown_callback(self.menu_mousedown)
            self.listener.set_mouseup_callback(self.menu_mouseup)
            self.listener.set_mousemove_callback(self.menu_mousemove)
        elif self.game_state == co.PLAY_STATE:
            self.listener.set_mousedown_callback(self.play_mousedown)
            self.listener.set_mouseup_callback(self.play_mouseup)
            self.listener.set_mousemove_callback(self.play_mousemove)
            
    def load_next_level(self):
        level = self.levels.get_next_level()
        self.launched_neutron = 0
        self.atoms = level[0].copy()
        self.level_text = level[1], level[2]
          
    def loop(self):
        dt = self.clock.tick(500)
        self.listener.listen()
        if self.game_state == co.MENU_STATE:
            self.draw_menu()
        elif self.game_state == co.PLAY_STATE:
            self.draw_game(dt)
            if self.is_level_over():
                pass
        pyg.display.flip()
            
    def draw_menu(self):
        self.screen.blit(self.menu, (0, 0))
            
    def draw_game(self, dt):
        self.screen.blit(self.background, (0, 0))
        
        self.draw_text()
        self.draw_neutron_count()
        
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
            
            
    def draw_text(self):
        if len(self.level_text[0]) > 0:
            util.draw_text(self.screen, self.level_text[0], co.TEXT_SIZE, (co.TEXT_X, co.TEXT_Y1), (0, 0, 0))
        if len(self.level_text[1]) > 0:
            util.draw_text(self.screen, self.level_text[1], co.TEXT_SIZE, (co.TEXT_X, co.TEXT_Y2), (0, 0, 0))
    
    def draw_player_arrow(self):
        if self.is_far_enough:
            pyg.draw.line(self.screen, co.ARROW_COLOR_FAR, (self.click_x, self.click_y), (self.mouse_x, self.mouse_y), co.ARROW_WIDTH)
        else:
            pyg.draw.line(self.screen, co.ARROW_COLOR_CLOSE, (self.click_x, self.click_y), (self.mouse_x, self.mouse_y), co.ARROW_WIDTH)
            
    def draw_neutron_count(self):
        self.screen.blit(textures.NEUTRON_TEXTURE.convert_alpha(), (co.NEUTRON_COUNT_X, co.NEUTRON_COUNT_Y))
        util.draw_text(self.screen, str(self.launched_neutron), co.NEUTRON_COUNT_TEXT_SIZE, (co.NEUTRON_COUNT_TEXT_X, co.NEUTRON_COUNT_TEXT_Y), (0, 0, 0))
            
            
    def menu_mousedown(self, x, y, button):
        if util.is_point_in_rect(co.LEVELS_BT, x, y):
            self.levels.restart()
            self.load_next_level()
            self.change_state(co.PLAY_STATE)
        elif util.is_point_in_rect(co.RANDOM_BT, x, y):
            pass
        elif util.is_point_in_rect(co.QUIT_BT, x, y):
            self.stopping()
        pass
        
    def menu_mouseup(self, x, y, button):
        pass
        
    def menu_mousemove(self, x, y, dx, dy):
        pass
        
    def play_mousedown(self, x, y, button):
        if button == co.LEFT_CLICK:
            if y > co.HEIGHT:
                return
            self.is_clicking = True
            self.click_x = x
            self.click_y = y
        if button == co.RIGHT_CLICK:
            self.is_clicking = False
    
    def play_mouseup(self, x, y, button):
        if button != co.LEFT_CLICK:
            return
        if self.can_play and self.is_clicking and self.is_far_enough:
            self.generate_neutron()
        self.is_clicking = False
        self.click_x = -1
        self.click_y = -1
    
    def play_mousemove(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
    
    
    def generate_neutron(self):
        self.launched_neutron += 1
        angle = math.pi/2 - math.atan2(self.mouse_x - self.click_x, (self.mouse_y - self.click_y))
        vx, vy = util.polar_to_cartesian(co.NEUTRON_SPEED, angle)
        neutron = neutrons.Neutron(self.click_x, self.click_y, vx, vy)
        self.neutrons.append(neutron)
    
    def is_level_over(self):
        return (sum(atom.over for atom in self.atoms) == 0) and (len(self.neutrons) == 0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
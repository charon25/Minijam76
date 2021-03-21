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
import _sounds_manager_ as sounds_manager
import util
import time, math

class Game():
    def __init__(self):
        self.is_ended = False
    
    def start(self):
        pyg.init()
        pyg.mixer.init()
        pyg.display.set_caption(co.SCREEN_TITLE)
        self.screen = pyg.display.set_mode(co.SCREEN_SIZE)
        pyg.display.set_icon(textures.NEUTRON_TEXTURE.convert_alpha())
        #Textures
        self.background = textures.BACKGROUND_TEXTURE.convert_alpha()
        self.menu = textures.MENU_TEXTURE.convert_alpha()
        self.eol = textures.EOL_TEXTURE.convert_alpha()
        self.eog = textures.EOG_TEXTURE.convert_alpha()
        self.restart_bt = textures.RESTART_BT_TEXTURE.convert_alpha()
        self.help = textures.HELP_TEXTURE.convert_alpha()
        #Listener
        self.listener = events.EventListener()
        self.listener.set_quit_callback(self.stopping)
        self.listener.set_sound_callback(self.play_sound)
        #Sons
        self.sounds = sounds_manager.SoundManager()
        self.sounds.start_music()
        #Etat
        self.game_state = None
        self.change_state(co.MENU_STATE)
        self.play_mode = None
        self.levels = levels_manager.Levels()
        self.level_text = ["", ""]
        self.level_required_neutrons = -1
        self.is_menu_drawn = False
        #Horloge
        self.clock = pyg.time.Clock()
        self.time_since_over = 0
        #Objets
        self.neutrons = []
        self.launched_neutrons = 0
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
        
    def play_sound(self, sound):
        self.sounds.play_sound(sound)
        
    def change_state(self, new_state):
        self.game_state = new_state
        if self.game_state == co.MENU_STATE:
            self.is_menu_drawn = False
            self.listener.set_mousedown_callback(self.menu_mousedown)
            self.listener.set_mouseup_callback(self.void)
            self.listener.set_mousemove_callback(self.void)
        elif self.game_state == co.PLAY_STATE:
            self.listener.set_mousedown_callback(self.play_mousedown)
            self.listener.set_mouseup_callback(self.play_mouseup)
            self.listener.set_mousemove_callback(self.play_mousemove)
        elif self.game_state == co.EOL_STATE:
            self.sounds.play_sound("eol")
            self.listener.set_mousedown_callback(self.eol_mousedown)
            self.listener.set_mouseup_callback(self.void)
            self.listener.set_mousemove_callback(self.void)
        elif self.game_state == co.EOG_STATE:
            self.sounds.play_sound("eol")
            self.listener.set_mousedown_callback(self.eol_mousedown)
            self.listener.set_mouseup_callback(self.void)
            self.listener.set_mousemove_callback(self.void)
            
    def reset_screen(self):
        self.neutrons = []
        self.launched_neutrons = 0
        self.atoms = []
        self.electrons = []
        self.change_state(co.PLAY_STATE)
            
    def load_level(self, level):
        self.reset_screen()
        self.atoms = level[0].copy()
        self.level_text = level[1], level[2]
        self.level_required_neutrons = level[3]
        
    def load_next_level(self):
        self.load_level(self.levels.get_next_level())
        
    def restart_level(self):
        self.load_level(self.levels.get_current_level())
        
    def load_random_level(self):
        self.load_level(self.levels.create_random_level())
        
    def restart_random_level(self):
        self.load_level(self.levels.reload_last_level())
    
          
    def loop(self):
        dt = self.clock.tick(500)
        self.listener.listen()
        if self.game_state == co.MENU_STATE:
            self.draw_menu()
        elif self.game_state == co.PLAY_STATE:
            self.draw_game(dt)
            pyg.display.flip()
            if self.is_level_over():
                if self.play_mode == co.RANDOM_MODE or self.levels.index < co.LEVELS_COUNT:
                    self.change_state(co.EOL_STATE)
                else:
                    self.change_state(co.EOG_STATE)
        elif self.game_state == co.EOL_STATE:
            self.draw_game(dt)
            self.draw_eol(False)
            pyg.display.flip()
        elif self.game_state == co.EOG_STATE:
            self.draw_game(dt)
            self.draw_eol(True)
            pyg.display.flip()
            
    def draw_menu(self):
        if not self.is_menu_drawn:
            self.screen.blit(self.menu, (0, 0))
            pyg.display.flip()
            self.is_menu_drawn = True
            
    def draw_game(self, dt):
        self.screen.blit(self.background, (0, 0))
        if self.play_mode == co.RANDOM_MODE or (self.play_mode == co.LEVEL_MODE and self.levels.index >= co.MIN_LEVEL_HELP):
            self.screen.blit(self.help, (co.HELP_X, co.HELP_Y))
        
        self.draw_text()
        
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
        
        self.can_play = (sum(atom.over for atom in self.atoms) > 0) and (self.game_state == co.PLAY_STATE)
        self.is_far_enough = (util.distance(self.click_x, self.click_y, self.mouse_x, self.mouse_y) >= co.MIN_DISTANCE_TO_PLAY)
        if self.is_clicking and self.can_play:
            self.draw_player_arrow()
                        
        if self.game_state == co.PLAY_STATE:
            self.draw_neutron_count()
            self.screen.blit(self.restart_bt, (co.RESTART_BT_X, co.RESTART_BT_Y))
            
        if sum(atom.over for atom in self.atoms) == 0:
            self.time_since_over += dt
        else:
            self.time_since_over = 0
            
            
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
        if self.launched_neutrons == 0:
            color = co.NEUTRON_COUNT_0_COLOR
        elif self.launched_neutrons < self.level_required_neutrons:
            color = co.NEUTRON_COUNT_LESS_COLOR
        elif self.launched_neutrons == self.level_required_neutrons:
            color = co.NEUTRON_COUNT_EQUAL_COLOR
        elif self.launched_neutrons > self.level_required_neutrons:
            color = co.NEUTRON_COUNT_MORE_COLOR
        
        if self.level_required_neutrons > 0:
            util.draw_text(self.screen,
                           "{}/{}".format(self.launched_neutrons, self.level_required_neutrons),
                           co.NEUTRON_COUNT_TEXT_SIZE,
                           (co.NEUTRON_COUNT_TEXT_X,co.NEUTRON_COUNT_TEXT_Y),
                           color)
        else:
            util.draw_text(self.screen,
                           str(self.launched_neutrons),
                           co.NEUTRON_COUNT_TEXT_SIZE,
                           (co.NEUTRON_COUNT_TEXT_X,co.NEUTRON_COUNT_TEXT_Y),
                           co.NEUTRON_COUNT_0_COLOR)
        
    def draw_eol(self, is_last_level):
        if not is_last_level:
            self.screen.blit(self.eol, (co.EOL_X, co.EOL_Y))
        else:
            self.screen.blit(self.eog, (co.EOL_X, co.EOL_Y))
        
        if self.level_required_neutrons > 0:
            util.draw_text(self.screen, str(self.level_required_neutrons), co.EOL_TEXT_SIZE, (co.EOL_REQUIRED_TEXT_X, co.EOL_REQUIRED_TEXT_Y), co.NEUTRON_COUNT_0_COLOR)
        else:
            util.draw_text(self.screen, "?", co.EOL_TEXT_SIZE, (co.EOL_REQUIRED_TEXT_X, co.EOL_REQUIRED_TEXT_Y), co.NEUTRON_COUNT_0_COLOR)
        
        if self.level_required_neutrons < 1:
            color = co.NEUTRON_COUNT_0_COLOR
        elif self.launched_neutrons < self.level_required_neutrons:
            color = co.NEUTRON_COUNT_LESS_COLOR
        elif self.launched_neutrons == self.level_required_neutrons:
            color = co.NEUTRON_COUNT_EQUAL_COLOR
        elif self.launched_neutrons > self.level_required_neutrons:
            color = co.NEUTRON_COUNT_MORE_COLOR
        util.draw_text(self.screen, str(self.launched_neutrons), co.EOL_TEXT_SIZE, (co.EOL_NUMBER_TEXT_X, co.EOL_NUMBER_TEXT_Y), color)
            
    def menu_mousedown(self, x, y, button):
        if button != co.LEFT_CLICK:
            return
        if util.is_point_in_rect(co.LEVELS_BT, x, y):
            self.sounds.play_sound("click")
            self.play_mode = co.LEVEL_MODE
            self.levels.restart()
            self.load_next_level()
        elif util.is_point_in_rect(co.RANDOM_BT, x, y):
            self.sounds.play_sound("click")
            self.play_mode = co.RANDOM_MODE
            self.load_random_level()
        elif util.is_point_in_rect(co.QUIT_BT, x, y):
            self.stopping()
    
    def eol_mousedown(self, x, y, button):
        if button != co.LEFT_CLICK:
            return
        if util.is_point_in_rect(co.EOL_MENU_BT, x, y):
            self.sounds.play_sound("click")
            self.change_state(co.MENU_STATE)
        elif util.is_point_in_rect(co.EOL_RESTART_BT, x, y):
            self.sounds.play_sound("click")
            if self.play_mode == co.LEVEL_MODE:
                self.restart_level()
            elif self.play_mode == co.RANDOM_MODE:
                self.restart_random_level()
        elif util.is_point_in_rect(co.EOL_NEXT_BT, x, y) and self.game_state == co.EOL_STATE:
            self.sounds.play_sound("click")
            if self.play_mode == co.LEVEL_MODE:
                self.load_next_level()
            elif self.play_mode == co.RANDOM_MODE:
                self.load_random_level()
        
    def void(self, **kwargs):
        pass
        
    def play_mousedown(self, x, y, button):
        if button == co.LEFT_CLICK:
            if y > co.HEIGHT:
                return
            if util.is_point_in_rect(co.RESTART_BT, x, y):
                self.sounds.play_sound("click")
                if self.play_mode == co.LEVEL_MODE:
                    self.restart_level()
                elif self.play_mode == co.RANDOM_MODE:
                    self.restart_random_level()
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
        self.sounds.play_sound("launch-neutron")
        self.launched_neutrons += 1
        angle = math.pi/2 - math.atan2(self.mouse_x - self.click_x, (self.mouse_y - self.click_y))
        vx, vy = util.polar_to_cartesian(co.NEUTRON_SPEED, angle)
        neutron = neutrons.Neutron(self.click_x, self.click_y, vx, vy)
        pyg.event.post(pyg.event.Event(555555, {}))
        self.neutrons.append(neutron)
    
    def is_level_over(self):
        return self.time_since_over > co.TIME_WITHOUT_ACTION
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pygame as pyg
import co

class SoundManager():
    def __init__(self):
        self.sounds = {}
        self.sounds["click"] = pyg.mixer.Sound(co.CLICK_PATH)
        self.sounds["launch-neutron"] = pyg.mixer.Sound(co.LAUNCH_NEUTRON_PATH)
        self.sounds["disintegration"] = pyg.mixer.Sound(co.DISINTEGRATION_PATH)
        self.sounds["fission"] = pyg.mixer.Sound(co.FISSION_PATH)
        self.sounds["absorb"] = pyg.mixer.Sound(co.ABSORB_PATH)
        self.sounds["wall"] = pyg.mixer.Sound(co.WALL_PATH)
        self.sounds["eol"] = pyg.mixer.Sound(co.EOL_SOUND_PATH)
        pyg.mixer.music.load(co.MUSIC_PATH)
    
    def play_sound(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()
        else:
            print("Unknown sound :", sound)
            
    def start_music(self):
        pyg.mixer.music.play(loops = -1)
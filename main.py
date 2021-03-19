import traceback
try:
    import pygame as pyg
    from _game_ import Game
    game = Game()
    
    
    #DEBUT
    game.start()
    
    while not game.is_ended:
        game.loop()
    
except:
    traceback.print_exc()
    game.stop()
else:
    game.stop()
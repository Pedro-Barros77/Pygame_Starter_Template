import pygame, sys


playing = False

def handle_events(game):
    """Iterates through each event and call it's appropriate function.
    Args:
        game (Game): The currently running game.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_app()
        elif event.type == pygame.KEYDOWN:
            handle_keydown(event.key, game)
        elif event.type == pygame.KEYUP:
            handle_keyup(event.key, game)
                
                
def handle_keydown(key, game):
    """Decides what to do with the key pressed by the user.
    Args:
        key (int): The pygame keycode of the key.
        game (Game): The currently running game.
    """
    if key not in game.pressed_keys:
        game.pressed_keys.append(key)
    

def handle_keyup(key, game):
    """Decides what to do with the key released by the user.
    Args:
        key (int): The pygame keycode of the key.
        game (Game): The currently running game.
    """
    if key in game.pressed_keys:
        game.pressed_keys.remove(key)

def quit_app():
    """Stops the game and closes application.
    """
    pygame.display.quit()
    pygame.quit()
    sys.exit()
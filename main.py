import os
import random

from casting.actor import Actor
from casting.gem import Gem
from casting.rock import Rock
from casting.cast import Cast

from director import Director

from services.keyboard_services import KeyboardService
from services.video_service import VideoService

from shared.color import Color
from shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_GEMS = 40
DEFAULT_ROCKS = 40

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)

    #create the rocks
    # x = int(MAX_X / 2)
    # y = int(MAX_Y - CELL_SIZE)
    # position = Point(x, y)

    # rocks = Rock()

    #create the gems
    # x = int(MAX_X / 2)
    # y = int(MAX_Y - CELL_SIZE)
    # position = Point(x, y)
    # gems = Gem()
    
    # # create the rocks
    # with open(DATA_PATH) as file:
    #     data = file.read()
    

    # # create the gems
    # with open(DATA_PATH) as file:
    #     data = file.read()

    # create the gems
    for gem in range(DEFAULT_GEMS):
        gem = Gem()
        gem.display()
        # gem.get_score()
        # gem.set_score()
        gem.collide()

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        
        #gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        gem.set_position(position)
        # gem.set_message(message)
        cast.add_actor("gems", gem)

    for rock in range(DEFAULT_ROCKS):
        rock = Rock()
        rock.display()
        # rock.get_score()
        # rock.set_score()
        rock.collide()

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        
        #gem.set_text(text)
        rock.set_font_size(FONT_SIZE)
        rock.set_position(position)
        # gem.set_message(message)
        cast.add_actor("rocks", rock)

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()

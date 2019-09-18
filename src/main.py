import configparser
from capture import grab_screen
import sys

def main(config_filename = "config.ini"):
    config = configparser.ConfigParser()
    config.read(config_filename)

    screen_cfg = config['ScreenConfig']
    screen_top = screen_cfg['top']
    screen_left = screen_cfg['left']
    screen_width = screen_cfg['width']
    screen_height = screen_cfg['height']
    grab_screen(screen_top, screen_left, screen_width, screen_height)


if __name__ == "__main__":
    main(sys.argv[1])
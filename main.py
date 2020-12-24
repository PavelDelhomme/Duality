from abc import ABCMeta

import pyglet
from pyglet.window import key

from player import Player
from game import Game
from assets import kiko_standby, background_img

import os


class MainWindow(pyglet.window.Window):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.set_caption("Duality")
        self.set_size(1920, 997)
        self.set_location(1, 30) # Initialize the location of the window
        self.label = pyglet.text.Label("This is the Main window")
        self.keys = key.KeyStateHandler()
        self.push_handlers(key)

        """Create an batch to manipulate graphics"""
        self.batch = pyglet.graphics.Batch()

        """Create two groups : 
        - the first is to display the background elements
        - the second is to display every each other element in to the first plan
        with priority to display"""
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        """Initialize images to load"""
        #todo move to assets.py...
        self.image_kiko = kiko_standby
        self.background_image = background_img

        #todo see here... https://pyglet.readthedocs.io/en/latest/programming_guide/image.html
        self.sprites = [pyglet.sprite.Sprite(self.background, batch=self.batch),
                        pyglet.sprite.Sprite(self.)]

        """link image to sprite in Batch group"""
        self.sprite_background = pyglet.sprite.Sprite(img=self.background_image, group=self.background)
        self.sprite_foreground = pyglet.sprite.Sprite(img=self.image_kiko, group=self.foreground)

        """Initialize sprite to load"""
        #self.sprite = [pyglet.sprite.Sprite(self.background_image, batch=self.batch),
        #               pyglet.sprite.Sprite(self.image_kiko, batch=self.batch)]

        # self.sprite = pyglet.sprite.Sprite(img=kiko_standby_image)

    def on_draw(self):
        self.clear() # cleanup screen
        self.label.draw()   # draw label first
        self.batch.draw()   # draw every each other images

    def on_key_press(self, symbol, modifiers):
        print(symbol)

    def on_key_release(self, symbol, modifiers):
        print(symbol)

    def on_text_motion(self, motion):
        pass


if __name__ == '__main__':
    window = MainWindow()  # Open Main window
    # window_game = Game()  # Open second window
    pyglet.app.run()

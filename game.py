from abc import ABCMeta

import pyglet
from pyglet.window import key
from player import Player

#kiko_standby_image = pyglet.resource.image('assets/Kiko/standby/kiko_standby.png')


class Game(pyglet.window.Window):
    """
    Here it is the Game logic
    """

    def __init__(self):
        super().__init__()
        self.set_caption("Duality")
        self.set_size(1080, 720)
        # self.background = pyglet.image.load()
        self.sprite = pyglet.sprite.Sprite(img=kiko_standby_image)
        self.label = pyglet.text.Label("This is the Game Window")
        self.keys = key.KeyStateHandler()

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.sprite.draw()



    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_text_motion(self, motion):
        pass

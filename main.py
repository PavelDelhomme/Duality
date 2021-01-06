import pyglet
from pyglet import window
from pyglet.window import key
import win32api

game_window = pyglet.window.Window(1920, 1080, resizable=True)
game_window.set_caption('Duality')
keys = key.KeyStateHandler()
game_window.push_handlers(keys)
label = pyglet.text.Label('Hello, it\'s Duality Game',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width // 2, y=game_window.height // 3,
                          anchor_x='center', anchor_y='top')

# todo Ressources

"""Resources for the game"""
pyglet.resource.path = ['assets/']
pyglet.resource.reindex()

kiko_run = pyglet.resource.image("run_0.png")


def center_image(image):
    """Sets an image's anchor point to the center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


center_image(kiko_run)

print(pyglet.resource.path)


class Duality(pyglet):

    def __init__(self):
        super(Duality, self).__init__()
        self.is_running = True
        self.welcome_screen = pyglet.image.load("assets/images/Ecran d'acceuil Duality.jpg")
        self.lt_coucou = pyglet.text.Label("Hey")


    def on_draw(self):
        game_window.clear()
        self.lt_coucou.draw()



    def run(self):
        self.is_running = True
        self.on_draw()


class Personnage(pyglet.sprite):
    def __init__(self, name):
        super(Duality.Personnage, self).__init__()
        self.name = name
        assert type(self.name) == str
        self.is_running = False
        assert type(self.is_running) == bool
        self.speed = 0
        assert type(self.speed) == int
        self.x = 0
        assert self
        self.y = 0
        assert self
        self.vx = [0, 0]
        assert self
        self.vy = [0, 0]
        assert self
        self.height = 0
        assert self
        self.witdh = 0
        assert self
        self.is_attacking = False
        assert type(self.is_attacking) == bool
        self.number_attacks = 0
        assert type(self.number_attacks) == int
        self.image = pyglet.image.load(None)
        assert type(self.image) == type(pyglet.image.AbstractImage)

    def attack(self):
        if not self.is_attacking:
            # Define some attacks
            pass

    def center_image(self, image):
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        return image


class Kiko(Personnage):
    def __init__(self, name):
        super().__init__(name)
        super(Duality.Personnage, self).__init_subclass__()
        self.name = "Kiko"
        self.is_running = False
        self.speed = 4
        self.speed = 5
        self.x = None
        self.y = None
        self.vx = None
        self.vy = None
        self.witdh = None
        self.height = None
        self.image = None
        self.number_attacks = None
        self.is_attacking = None
        self.a = None

    def attack(self):
        pass

    def special_attack(self):
        pass


class Drya(Personnage):
    def __init__(self, name):
        super().__init__(name)
        super(Duality.Personnage, self).__init_subclass__()
        self.name = "Drya"
        self.is_running = False
        self.speed = 5
        self.x = None
        self.y = None
        self.vx = None
        self.vy = None
        self.witdh = None
        self.height = None
        self.image = None
        self.number_attacks = None
        self.is_attacking = None
        self.a = None

    def attack(self):
        pass

    def special_attack(self):
        pass


@game_window.event
def on_draw():
    game_window.clear()
    label.draw()
    if keys[key.SPACE]:
        print("Space key was pressed")

    kiko_run.blit(0, 0)


if __name__ == '__main__':
    pyglet.app.run()

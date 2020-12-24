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
                          x=game_window.width//2, y=game_window.height//3,
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


# center_image(kiko_run)

print(pyglet.resource.path)


@game_window.event
def on_draw():
    game_window.clear()
    label.draw()
    if keys[key.SPACE]:
        print("Space key was pressed")

    kiko_run.blit(0, 0)


if __name__ == '__main__':
    pyglet.app.run()

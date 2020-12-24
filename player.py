import pyglet


class Player:
    """
    Here is the abstraction of an Player
    """

    def __init__(self):
        self.pos = None
        self.pos.x = None
        self.pos.y = None
        self.attack = None
        self.special_attack = None
        self.is_moving = False
        self.is_jumping = False
        self.is_standing = True
        self.is_attacking = False

    def attack(self, damage):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def jumping(self):
        pass


import pygame as pg

class Object(pg.sprite.Sprite):
    """represents the visible objects in the game"""
    def __init__(self, image):
        super().__init__()
        self.image = image                          
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.position = pg.math.Vector2(0,0)
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)

    def update(self):
        pass






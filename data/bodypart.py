from data.object import Object
import pygame as pg
import random 
import data.config as cng
import math

class BodyPart(Object):
    def __init__(self, image, x, y):
        super().__init__(image)
        self.position = pg.math.Vector2(x-self.image.get_width(), y-self.image.get_height())
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)
       

    def draw(self, surface):
        """Draw the body part on the given surface."""
        surface.blit(self.image, self.rect)  # Draw the image at its rect position

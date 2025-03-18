import pygame as pg

class Mouse(pg.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = image
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pg.rect.Rect(0,0, width, height) # get rect

    def update(self):
        mouse = pg.mouse.get_pos() #hente posisjon til musa
        new_x = mouse[0] #mouse på plass 0 er x verdi i tuppel i pos, 1 er y verdi
        new_y = mouse[1] - 0.25 * self.image.get_height() #for å flytte musepeker i midten av bildet
        self.rect.x = new_x
        self.rect.y = new_y
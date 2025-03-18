import pygame as pg
import random
import data.config as cng

class Letter(pg.sprite.Sprite):
    """Represents a letter."""
    def __init__(self, font, pos_x, pos_y, text):
        super().__init__()
        self.position = pg.math.Vector2(pos_x, pos_y) 
        self.color = (0, 0, 0)  # Black
        self.text = text.upper()
        self.letter_surface = font.render(self.text, True, self.color)
        #print(f"Letter created: {self.text}")

    def draw(self, surface):
        """Draw the letter on the given surface."""
        surface.blit(self.letter_surface, self.position)  # Tegner bokstaven på overflaten



class GuessLetter(Letter):
    """Letter that user click to guess"""
    def __init__(self, font, pos_x, pos_y, text):
        super().__init__(font, pos_x, pos_y, text)
        self.rect = self.letter_surface.get_rect(topleft=(pos_x, pos_y))
        self.font = font

    def wrong_guess(self):
        """Endrer fargen på bokstaven når det gjøres en feil gjetning."""
        self.color = (255, 0, 0)  # Rød
        self.update_surface()  # Oppdater overflaten for å gjenspeile fargeendringen

    def correct_guess(self):
        """Endrer fargen på bokstaven når det gjøres en korrekt gjetning."""
        self.color = (0, 255, 0)  # Grønn
        self.update_surface()  # Oppdater overflaten for å gjenspeile fargeendringen
    
    def reset_guess(self):
        """Resetter fargen på bokstaven når man begynner på nytt"""
        self.color = (0,0,0) # svart
        self.update_surface()

    def update_surface(self):
        """Oppdaterer overflaten til bokstaven etter fargeendring."""
        self.letter_surface = self.font.render(self.text, True, self.color)  # Oppdater overflaten
    

class LineLetter(Letter):
    """"Letter that appear on line when guessed"""
    def __init__(self, font, pos_x, pos_y, text):
        super().__init__(font, pos_x, pos_y, text)
    



class Line:
    def __init__(self, font, screen, start_x, start_y, end_x, end_y, letter):
        self.font = font
        self.screen = screen
        self.letter = letter
        self.guessed = False
        self.start_pos = (start_x, start_y)
        self.end_pos = (end_x, end_y)
        self.letter_instance = None  # Lagre bokstavinstansen her

    def draw(self):
        """Tegner linjen."""
        pg.draw.line(self.screen, (0, 0, 0), self.start_pos, self.end_pos, 5)


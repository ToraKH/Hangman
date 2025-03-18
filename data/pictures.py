import config as cng
import pygame as pg

class BackgroundManager():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cng.SCREEN_X, cng.SCREEN_Y))
        self.load_backgrounds()
        self.load_arena_images()

    def load_backgrounds(self):
        """Load screen backgrounds"""
        backgrounds = {
            "start_bg": cng.START,
            "end_bg": cng.END,
            "custom_bg": cng.CUSTOM
        }

        self.backgrounds = {}
        for name, path in backgrounds.items():
            bg = pg.image.load(path)
            self.backgrounds[name] = pg.transform.scale(bg, (cng.SCREEN_X, cng.SCREEN_Y)).convert()

    def load_arena_images(self):
        """Load background images"""
        arena_images = [
            cng.BG1,
            cng.BG2,
            cng.BG3,
            cng.BG4,
            cng.BG5,
            cng.BG6
        ]

        self.arena_list = []
        for img_path in arena_images:
            arena_pic = pg.image.load(img_path).convert_alpha()
            scaled_arena_pic = pg.transform.scale(arena_pic, (arena_pic.get_width() // 15, arena_pic.get_height() // 15))
            self.arena_list.append(scaled_arena_pic)
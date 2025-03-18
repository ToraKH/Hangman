import pygame as pg
# from pygame import mixer
import data.config as cng


# ============================================================= 
def start_screen(screen, start_bg):
    """ Shows the start screen"""
    screen.blit(start_bg, (0,0)) 
    
    key = pg.key.get_pressed()

    # Start game if pressed on start button
    if key[pg.K_SPACE]:
        pg.time.delay(150)
        return True   #start game

    #-----------------------------------------------------
    
    # Blit text
    font1 =pg.font.SysFont(None, 21)
    font2 =pg.font.SysFont(None, 70)
    font3 =pg.font.SysFont(None, 40)

    title = font2.render('THE HANG MAN', True, (0,0,0))
    created_by = font1.render('A game by Tora K. Homme', True, (0,0,0))
    instr = font3.render('Press "SPACE" to start', True, (0,0,0))

    screen.blit(title, ((cng.SCREEN_X-title.get_width())/2, cng.SCREEN_Y/3+45))
    screen.blit(created_by, ((cng.SCREEN_X-created_by.get_width())/2, cng.SCREEN_Y-30))
    screen.blit(instr, ((cng.SCREEN_X-instr.get_width())/2, cng.SCREEN_Y-160))

    pg.display.update()    

# ============================================================= 

def show_finish(screen, bg, result, word, color):

    # result = 1 -> won
    # result = 2 -> lost
    # ask if want to restart
    screen.blit(bg, (0,0))
    key = pg.key.get_pressed()

    # Start game if pressed on start button
    if key[pg.K_SPACE]:
        pg.time.delay(150)
        return True   #start game

    

    font1 =pg.font.SysFont(None, 50)
    
    #-----------------------------------------------------
    
    #Create text in the correct font
    
    word_text = font1.render('THE WORD WAS ' + word.upper(), True, (color, color, color))

    #Print text at correct place of the screen
    screen.blit(word_text, ((cng.SCREEN_X-word_text.get_width())/2, 100))

    font3 =pg.font.SysFont(None, 40)
    instr = font3.render('Press "SPACE" to restart', True, (0,0,0))
    screen.blit(instr, ((cng.SCREEN_X-instr.get_width())/2, cng.SCREEN_Y-40))

    pg.display.update()    


    
# ============================================================= 
def show_credit(screen, credit_bg):
    screen.blit(credit_bg, (0,0))
    font2 =pg.font.SysFont(None, 50)
    font1 =pg.font.SysFont(None, 30)
    
    #-----------------------------------------------------
    
    #Create text in the correct font
    credit_title = font2.render('CREDITS', True, (0,0,0))

    creators = font1.render('DEVELOPER & SUPPORT', True, (0,0,0))
    game_devs = font1.render('Game developer: Tora K. Homme', True, (0,0,0))

    images = font1.render('IMAGES', True, (0,0,0))
    body = font1.render('Body by: Sigurd A. Lorentzen' , True, (0,0,0))
    bg = font1.render('Background by: Tora K. Homme' , True, (0,0,0))

    #-----------------------------------------------------

    #Print text at correct place of the screen
    screen.blit(credit_title, ((cng.SCREEN_X-credit_title.get_width())/2, 4*credit_title.get_height()))

    screen.blit(creators, ((cng.SCREEN_X-creators.get_width())/2, 11* creators.get_height()))
    screen.blit(game_devs, ((cng.SCREEN_X-game_devs.get_width())/2, 13*game_devs.get_height()))


    screen.blit(images, ((cng.SCREEN_X-images.get_width())/2, 17*body.get_height()))
    screen.blit(body, ((cng.SCREEN_X-body.get_width())/2, 19*body.get_height()))
    screen.blit(bg, ((cng.SCREEN_X-bg.get_width())/2, 21*bg.get_height()))


    pg.display.update() 
    pg.time.delay(2000)
    # Exit game if pressed
    exit()

def show_text(screen, lives):
    """Prints text on screen"""
    # Register chosen font + its size and Create text for game-stats 
    font =pg.font.SysFont(None, 50)
    score_player1 = font.render('LIVES LEFT ' + str(lives), True, (255,255,255))
    screen.blit(score_player1, (cng.SCREEN_X/2, 100))
    
    font2 = pg.font.SysFont(None, 30)
    instruction = font2.render('Press the letters on the left to guess', True, (0,0,0))
    screen.blit(instruction, ((cng.SCREEN_X-instruction.get_width())-30, cng.SCREEN_Y-30))

    
    




# ============================================================= 

# def play_music():
    # """Plays the music"""
    # #Initialise pygame music mixer
    # mixer.init()
    # #Load chosen music-file
    # mixer.music.load((cng.MUSIC))
    # #Adjust volume
    # mixer.music.set_volume(cng.VOLUME)
    # #Play music from the beginning
    # mixer.music.play(-1, 0, 0)
    
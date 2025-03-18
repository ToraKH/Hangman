import pygame as pg
import data.config as cng
from data.bodypart import BodyPart
# from data.letter import Letter
import data.interface as interface
from data.line import Line, GuessLetter, LineLetter
from data.mouse import Mouse
# from random_word import RandomWords

import random
import time



class Manager():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cng.SCREEN_X, cng.SCREEN_Y))
        self.clock = pg.time.Clock()

        self.font = pg.font.SysFont(None, 70)
        self.BIGfont = pg.font.SysFont(None, 40)
        self.LINEfont = pg.font.SysFont(None, 50)


        self.wrong_guess_counter = 0
        self.guessed_letters = []
        # self.correct_guessed_letters = []
        self.num_letters_guessed_correctly = 0 


        # Sett ulike kroppsdele flaggene til falsk, slik at man ikke tegner de før man har gjettet feil
        self.Leftarm = False
        self.Rightarm = False
        self.Leftleg = False
        self.Rightleg = False
        self.body_flag = False
        self.head_flag = False

        self.last_guess_time = 0  # Initialize timestamp for last guess
        self.cooldown = 1  # Set cooldown in seconds

        self.result = 0



        self.game = "starting"
        self.load_images()
        self.index = random.randint(0,4)
        self.game_bg = self.bg_img[self.index]
        self.sprite_init()
        self.place_letters()
        # interface.play_music() 
        self.loop()
        
        
    

    def load_images(self):
        """Loads and scales the images"""

        # Load body parts
        self.arm_left_img = pg.image.load(cng.ARM).convert_alpha() 
        self.arm_left_img = pg.transform.scale(self.arm_left_img,(cng.scaling*(self.arm_left_img.get_width()/3), cng.scaling*self.arm_left_img.get_height()/3))
        self.arm_left_img = pg.transform.flip(self.arm_left_img, True, False)


        self.arm_right_img = pg.image.load(cng.ARM).convert_alpha() 
        self.arm_right_img = pg.transform.scale(self.arm_right_img,(cng.scaling*(self.arm_right_img.get_width()/3), cng.scaling*self.arm_right_img.get_height()/3))

        self.leg_left_img = pg.image.load(cng.LEFTLEG).convert_alpha() 
        self.leg_left_img = pg.transform.scale(self.leg_left_img,(cng.scaling*(self.leg_left_img.get_width()/3), cng.scaling*self.leg_left_img.get_height()/3))

        self.leg_right_img = pg.image.load(cng.RIGHTLEG).convert_alpha() 
        self.leg_right_img = pg.transform.scale(self.leg_right_img,(cng.scaling*(self.leg_right_img.get_width()/3), cng.scaling*self.leg_right_img.get_height()/3))

        self.head_img = pg.image.load(cng.HEAD).convert_alpha() 
        self.head_img = pg.transform.scale(self.head_img,(cng.scaling*(self.head_img.get_width()/3), cng.scaling*self.head_img.get_height()/3))

        self.body_img = pg.image.load(cng.BODY).convert_alpha() 
        self.body_img = pg.transform.scale(self.body_img,(cng.scaling*(self.body_img.get_width()/3), cng.scaling*self.body_img.get_height()/3))

        self.mouse_img = pg.image.load(cng.MOUSE).convert_alpha()
        self.mouse_img = pg.transform.scale(self.mouse_img,(cng.scaling*(self.mouse_img.get_width()/3), cng.scaling*self.mouse_img.get_height()/3))


        # Load backgrounds
        self.start_bg = pg.image.load(cng.START)
        self.start_bg = pg.transform.scale(self.start_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.start_bg.convert()
        self.win_bg = pg.image.load(cng.WIN)
        self.win_bg = pg.transform.scale(self.win_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.win_bg.convert()
        self.credit_bg = pg.image.load(cng.CREDIT)
        self.credit_bg = pg.transform.scale(self.credit_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.credit_bg.convert()

        self.lose_bg = pg.image.load(cng.LOSE)
        self.lose_bg = pg.transform.scale(self.lose_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.lose_bg.convert()



        # Load game backgrounds
        self.bg_img = [
            pg.image.load(cng.BG1).convert_alpha(),
            pg.image.load(cng.BG2).convert_alpha(),
            pg.image.load(cng.BG3).convert_alpha(),
            pg.image.load(cng.BG4).convert_alpha(),
            pg.image.load(cng.BG5).convert_alpha()
        ]

        # Scale and convert images
        self.bg_img = [pg.transform.scale(img, (cng.SCREEN_X, cng.SCREEN_Y)) for img in self.bg_img]
        self.bg_img = [img.convert() for img in self.bg_img]


    def sprite_init(self):
        """Initializes sprite objects"""
        angle = 15
        self.armL = BodyPart(pg.transform.rotate(self.arm_left_img, -angle), cng.SCREEN_X - 169, cng.SCREEN_Y - 283)
        self.armR = BodyPart(pg.transform.rotate(self.arm_right_img, angle), cng.SCREEN_X - 40, cng.SCREEN_Y - 285)
        self.legL = BodyPart(self.leg_left_img, cng.SCREEN_X - 140, cng.SCREEN_Y - 150)
        self.legH = BodyPart(self.leg_right_img, cng.SCREEN_X - 100, cng.SCREEN_Y - 150)
        self.body = BodyPart(self.body_img, cng.SCREEN_X-75, cng.SCREEN_Y-300)
        self.head = BodyPart(self.head_img, cng.SCREEN_X-75, cng.SCREEN_Y-400)

        self.mouse = Mouse(self.mouse_img)
        self.mouse_group = pg.sprite.Group()
        self.mouse_group.add(self.mouse)

        self.letter_group = pg.sprite.Group()

        self.line_list = []



    def place_letters(self):
        """Places the letters on the screen"""      
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.letter_sprites = {}
        start_x = 50
        start_y = 50
        
        #distance between letters
        x_spacing = 60
        y_spacing = 60
        
        for index, letter in enumerate(self.letters):
            row = index // 4
            col = index % 4

            x = start_x + (col * x_spacing)
            y = start_y + (row * y_spacing)

            self.letter_sprites[letter] = GuessLetter(self.BIGfont, x, y, letter.upper())
            self.letter_group.add(self.letter_sprites[letter])
        
  

    def loop(self):
        """Main loop for manager. Checks the event for exit strategy, and
           updates all the objects""" 
        while True:
            # Process events
            for event in pg.event.get():
                    
                if event.type == pg.QUIT:
                    self.game = "credits"

                
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.game = "credits"
                    

            #--------------START-SCREEN--------------------------
                # Startscreen
            if self.game == "starting":

                # ensure that all quessing letters are default for (re)starting
                for letter in self.letter_group:
                    letter.reset_guess()

                self.line_list = []
                self.wrong_guess_counter = 0
                self.guessed_letters = []
                self.num_letters_guessed_correctly = 0 
                self.counter = 0

                # Sett ulike kroppsdele flaggene til falsk, slik at man ikke tegner de før man har gjettet feil
                self.Leftarm = False
                self.Rightarm = False
                self.Leftleg = False
                self.Rightleg = False
                self.body_flag = False
                self.head_flag = False

                self.last_guess_time = 0  # Initialize timestamp for last guess
                self.cooldown = 0.5  # Set cooldown in seconds
                self.result = 0
                self.index = random.randint(0,4)
                self.game_bg = self.bg_img[self.index]

                #Draw starting screen
                status = interface.start_screen(self.screen, self.start_bg)
                if status:
                    new_word = True
                    self.game = "on"
            #--------------GAME-SCREEN---------------------------
                    
            #Let the games begin...
            if self.game == "on":
                
                self.screen.blit(self.game_bg, (0,0)) 

                if new_word:
                    self.find_random_word()
                    new_word = False
                self.place_lines()

                
                if event.type == pg.MOUSEBUTTONDOWN: #hvis vi har klikket ned på museknappen, så:
                    mouse_pos = pg.mouse.get_pos()
                    for letter_sprite in self.letter_group:
                        # Sjekk om museposisjonen er innenfor rektangelet til bokstaven
                        if letter_sprite.rect.collidepoint(mouse_pos):
                            # Gjør noe med bokstaven som er klikket
                            self.check_validity(letter_sprite) 
                     
                    
                self.event()
                
                lives = 6-self.wrong_guess_counter
                interface.show_text(self.screen, lives)

                #Maintains 60 frames per second
                #Updates sprites
                self.update()
                self.clock.tick(60)

            #----------------END-SCREEN----------------------------
            if self.game == "won":
                pg.time.delay(300)
                status = interface.show_finish(self.screen, self.win_bg, self.result, self.word, 0)
                if status:
                    self.game = "starting"
            if self.game == "lost":
                pg.time.delay(300)
                status = interface.show_finish(self.screen, self.lose_bg, self.result, self.word, 0)
                if status:
                    self.game = "starting"
            if self.game == "credits":
                interface.show_credit(self.screen, self.credit_bg)


    def event(self):
        """pg event"""
        self.clock.tick(60)  # Frames per second


    def load_words(self, filename):
        """Load words from a file and return a list of words."""
        with open(filename, 'r') as file:
            # Read all lines, strip whitespace, and filter out empty lines
            words = [line.strip() for line in file if line.strip()]
            
        file.close
        return words


    def get_random_word(self, words):
        """Return a random word from the list of words."""
        return random.choice(words)


    def find_random_word(self):
        """ Find a random word from the text file"""
        words_list = self.load_words('data/words.txt')
        self.word = self.get_random_word(words_list)
        self.word_length = len(self.word)
        print(f"Secret word: {self.word}")


    def place_lines(self):
        """ Place lines on screen based on the word"""
        index = 0
        start_x = cng.SCREEN_X/4
        end_x = cng.SCREEN_X/4+20
        start_y = cng.SCREEN_Y -50
        end_y = start_y
        x_distance = 50     #length between
        while(index < self.word_length):
           current_start_x = start_x +index*x_distance
           current_end_x = end_x +index*x_distance

            # Draw a line (surface, color, start_pos, end_pos, width)
           line = Line(self.font, self.screen, current_start_x, start_y, current_end_x, end_y, self.word[index]) 
           self.line_list.append(line)
           

           index += 1


    def count_letters(self, word, letter):
        self.counter = 0
        for bokstav in word:
            if bokstav.upper() == letter.upper():
                self.counter += 1
             

    # telle bokstavene i ordet og legge til så mange til guessed letters
    def check_validity(self, letter_sprite):
        """Sjekker om en bokstav finnes i ordet og oppdaterer linjene."""
        guess = letter_sprite.text
        # Prevent duplicate guesses
        if guess in self.guessed_letters:
            return  # Ignore this guess if the letter has already been guessed
        
        current_time = time.time()
        if current_time - self.last_guess_time < self.cooldown:
            # goes here if you click to fast
            return  # Ignore input if cooldown period hasn't passed

        self.last_guess_time = current_time  # Update last guess time

        # If the guess is correct
        if guess in self.word.upper():
            self.count_letters(self.word, guess)
            for line in self.line_list:
                if line.letter.upper() == guess:
                    line.guessed = True  # Mark the letter as guessed
                    start_x, start_y = line.start_pos
                    line.letter_instance = LineLetter(self.LINEfont, start_x, start_y - 40, guess)
                    letter_sprite.correct_guess()
                    
            # print(f"Correct guess: {guess}")


            print(self.counter)
            self.num_letters_guessed_correctly += self.counter
           
            # Check if the word is completed => player wins
            if self.num_letters_guessed_correctly == self.word_length:
                self.player_won()
            
        else:
            # Do nothing here if the letter has already been guessed
            # print(f"Wrong guess: {guess}")
            self.wrong_guess(letter_sprite)
        
        self.guessed_letters.append(guess)
        

    def player_won(self):
        """ Handles when player guessed correct word"""
        # print("PLAYER WON!")
        self.result = 1 #One for won
        self.game = "won"
        # print("======================================= WON")

    def wrong_guess(self, letter_sprite):
        """ Handles when a wrong guess is guessed"""
        self.wrong_guess_counter += 1 #increase number of wrong guesses
        letter_sprite.wrong_guess()
        if self.wrong_guess_counter == 1:
            #place head
            self.head_flag = True
        if self.wrong_guess_counter == 2:
            #place body
            self.body_flag = True
        if self.wrong_guess_counter == 3:
            #place Larm
            self.Leftarm = True
        if self.wrong_guess_counter == 4:
            #Place Rarm
            self.Rightarm = True
        if self.wrong_guess_counter == 5:
            #place Lleg
            self.Leftleg = True
        if self.wrong_guess_counter == 6:
            #place Rleg
            self.Rightleg = True
            #Show Lost, and end screen
            self.player_lost()

    def player_lost(self):
        """Handles when player lost"""   
        # print("PLAYER LOST!")
        self.result = 2 #2 for lost
        self.game = "lost"
        # print("======================================= LOST")

    def get_input(self):
        """ Get a letter from the user"""
        
        Q = self.font.render('Choose a letter', True, (0,0,0))
        self.screen.blit(Q, ((cng.SCREEN_X-Q.get_width())/2, cng.SCREEN_Y/3+45))
    
    def update(self):
        """Oppdaterer alle objekter gjennom sprite's group update."""
        
        # Tegner alle kroppsdeler hvis man skal
        if self.Leftarm:
            self.armL.draw(self.screen)
        if self.Rightarm:
            self.armR.draw(self.screen)
        if self.Leftleg:
            self.legL.draw(self.screen)
        if self.Rightleg:
            self.legH.draw(self.screen)
        if self.body_flag:
            self.body.draw(self.screen)
        if self.head_flag:
            self.head.draw(self.screen)

        # Tegner bokstavene
        for letter in self.letter_sprites.values():
            letter.draw(self.screen)
            
        # Tegner linjene og bokstavene
        for line in self.line_list:
            line.draw()       # Tegner linjen
            if line.letter_instance:
                line.letter_instance.draw(self.screen)# Tegner bokstaven hvis den er gjettet

        pg.display.update()


if __name__ == "__main__":
    Manager()
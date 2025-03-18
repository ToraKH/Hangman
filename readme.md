# Hangman
This is my implementation of a "hangman" game. "Hangman" is a game where you try to guess a word based on how many lines there are.
Each line represents one letter. 
If you guess the correct letter, every instance of that letter in the word will be put its line. 
If you guess the wrong letter, one part of the man is hanged, and you lose a life. 
The goal is to keep the man alive by guessing the correct letters, which will reveal the word.

### Author
Tora K. Homme

## Installing pygame
Ensure that python is installed

```bash
  python --version
```

Ensure that PIP is installed

```bash
  pip --version
```

Install pygame 

```bash
  pip install pygame
```

## Run the game
Ensure you are in the hangman directory

```bash
  cd hangman
```

Run simulation

```bash
  python3 manager.py
```

## Key Commands
```To start/restart, press SPACE```

```To exit, press ESC or the X in the top corner. This will show the credits, which will automatically exit after some seconds have passed```

```To guess the letters, click on the letters on the left with your mouse```


## Note
There are 5000 different english words to guess from. They are not checked, and can therefore be either very easy or very hard to quess. 
Hopefully, you get a good mix of difficulty.

Another thing to note is that there seem to be some unintentional delay sometimes. This seem to happen when trying to exit, or taking a quess too soon. If you press on a letter, and nothing happens (no color change), wait about 5 seconds and try again.

### Credits
All images are made by Tora K. Homme or Sigurd A. Lorentzen.
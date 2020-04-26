import random


class Hangman:

    def __init__(self):
        self.startMsg = "H A N G M A N"
        self.wordList = ['python', 'java', 'kotlin', 'javascript']
        self.word = random.choice(self.wordList)
        self.wordstr = ['-'] * len(self.word)
        self.lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self.guessedLetters = ''
        self.lives = 8
        self.guessed = False
        self.gameMsg = ["No improvements",
                        "No such letter in the word",
                        "You guessed the word!",
                        "You already typed this letter",
                        "It is not an ASCII lowercase letter",
                        "You should print a single letter"]
        self.endSuccessMsg = "You survived!"
        self.endFailureMsg = "You are hanged!"

    def reset(self):
        self.word = random.choice(self.wordList)
        self.wordstr = ['-'] * len(self.word)
        self.guessedLetters = ''
        self.lives = 8
        self.guessed = False

    def start(self):
        print(self.startMsg)
        while True:
            choice = input('Type "play" to play the game, "exit" to quit:')
            if choice == 'play':
                self.guess()
                print()
                self.reset()
            else:
                break

    def guess(self):
        while self.lives != 0 and self.guessed == False:
            self.nextTurn()
        if self.guessed == True:
            print(self.gameMsg[2])
            print(self.endSuccessMsg)
        else:
            print(self.endFailureMsg)

    def nextTurn(self):
        print()
        print(''.join(self.wordstr))
        letter = input("Input a letter:")
        if len(letter) > 1:
            print(self.gameMsg[5])
            return
        elif letter in self.guessedLetters:
            print(self.gameMsg[3])
            return
        elif letter not in self.lowercase:
            print(self.gameMsg[4])
            return
        else:
            self.guessedLetters += letter
        if letter in self.word and letter in self.wordstr:
            print(self.gameMsg[0])
            self.lives -= 1
        elif letter not in self.word:
            print(self.gameMsg[1])
            self.lives -= 1
        else:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.wordstr[i] = letter
        if '-' not in self.wordstr:
            self.guessed = True


game = Hangman()
game.start()
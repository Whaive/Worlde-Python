import random

class Wordle:

    word = "TESTE"
    allWords = []
    guesses = []
    MAX_LENGTH = 5
    tries = 0
    win = False

    def __init__(self, tries):
        self.tries = tries

        with open("words.txt", "r") as f:

            for el in f:
                self.allWords.append(el.strip().upper())

        self.word = random.choice(self.allWords)
        

    def guess(self, guess):
        
        guess = guess.upper() # Convert Word

        # Checks for valid size word
        if len(guess) != self.MAX_LENGTH or self.allWords.count(guess) <= 0:
            return False
        
        # Store the word in the array
        self.guesses.append(guess)
        return True


    # Check if the number of tries has reached the limit
    def gameOver(self):

        lastGuess = len(self.guesses) - 1
        if lastGuess < 0:
            return False

        if len(self.guesses) == self.tries:
            return True
        
        if self.guesses[lastGuess] == self.word:
            self.win = True
            return True



        




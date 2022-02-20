class Display:
    
    normal = "\033[0m"
    bold = "\033[1m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"

    tries = 0

    word = ""
    board = []

    def __init__(self, word, tries):
        self.word = word
        self.tries = tries

        display = self.normal + "_ _ _ _ _"
        for i in range(tries):

            self.board.append(display)


    def addBoard(self, guess, index):

        display = ""

        for i in range(len(self.word)):
            

            # Mark Letters in the right spot
            if guess[i] == self.word[i]:
                display += self.green + guess[i] + " "
            # Mark Letters in the word but in the wrong spot
            elif self.word.count(guess[i]):
                display += self.yellow + guess[i] + " "
            else:
                display += self.normal + guess[i] + " "

        display = display.strip()
        self.board[index] = display


    def showBoard(self):
        for el in self.board:
            print(el)


    def gameOver(self, win):

        if win:
            print("\n" + self.green + "Correct!\nThe Word was: " + self.bold + self.word + self.normal)
            return
        
        print("\n" + self.red + "Out of Tries!\nThe Word was: " + self.bold + self.word + self.normal)


    def error(self):
        print(self.red + "Not in the words list" + self.normal)

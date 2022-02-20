from Wordle import Wordle
from display import Display

tries = 6

def main():

    wordle = Wordle(tries)
    display = Display(wordle.word, tries)

    while True:

        display.showBoard()

        if wordle.gameOver():
            display.gameOver(wordle.win)
            break

        word = input("\n> ")

        if wordle.guess(word) == False:
            display.error()
            continue
        
        lastIndex = len(wordle.guesses) - 1
        display.addBoard(wordle.guesses[lastIndex], lastIndex)











if __name__ == "__main__":
    main()
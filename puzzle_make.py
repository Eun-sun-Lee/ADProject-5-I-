from word import Word
from puzzle_load_words import Puzzle_load_words
import random

class Puzzle_make:
    def __init__(self):
        self.common_point = None
        while self.common_point == None:
            secretwords = Word('word.txt')
            self.word1 = secretwords.randFromDB()
            self.word2 = secretwords.randFromDB()
            while self.word1 == self.word2:
                self.word2 = secretwords.randFromDB()

            puzzle = Puzzle_load_words()
            self.common_point = puzzle.puzzle_word_generate(self.word1, self.word2)

    def make_puzzle(self):
        word1 = self.word1
        word2 = self.word2
        common_x = self.common_point[0]
        common_y = self.common_point[1]

        puzzle_board = [['_']*len(word1) for _ in range(len(word2))]
        puzzle_board[common_y][common_x] = word1[common_x]

        location_x = [i for i in range(len(word1))]
        location_y = [i for i in range(len(word2))]
        location_x.remove(common_x)
        location_y.remove(common_y)

        i = 0
        while i < (len(word1)-1)/2:
            random_index = random.randrange(0, len(location_x))
            puzzle_board[common_y][location_x[random_index]] = word1[location_x[random_index]]
            location_x.pop(random_index)
            i += 1

        i = 0
        while i < (len(word2)-1)/2:
            random_index = random.randrange(0, len(location_y))
            puzzle_board[location_y[random_index]][common_x] = word2[location_y[random_index]]
            location_y.pop(random_index)
            i += 1

        for i in range(len(puzzle_board)):
            print(puzzle_board[i])

puzzle_make  = Puzzle_make()
puzzle_make.make_puzzle()

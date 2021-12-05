from word import Word
from puzzle_load_words import Puzzle_load_words
import random

class Puzzle_make:
    def __init__(self):
        self.common_point = None
        while self.common_point == None: # 두 단어의 공통지점이 있을떄까지 반복
            secretwords = Word('word.txt')
            self.word1 = secretwords.randFromDB() # word1 뽑기
            self.word2 = secretwords.randFromDB() # word2 뽑기
            while self.word1 == self.word2: # word1과 word2가 다를때까지 word2를 뽑기
                self.word2 = secretwords.randFromDB()

            puzzle = Puzzle_load_words()
            self.common_point = puzzle.puzzle_word_generate(self.word1, self.word2) # 두 단어의 공통 지점을 가져오기
    def make_puzzle(self):
        word1 = self.word1 # 첫번쨰 단어
        word2 = self.word2 # 두번째 단어
        common_x = self.common_point[0] # 첫번째 단어에서 겹치는 문자의 index
        common_y = self.common_point[1] # 첫번째 단어에서 겹치는 문자의 index

        self.puzzle_board = [['#']*len(word1) for _ in range(len(word2))] # puzzle 생성 (모두 #으로 초기화)
        self.puzzle_board[common_y][common_x] = word1[common_x] # 겹치는 문자를 puzzle에 표시

        location_x = [i for i in range(len(word1))] ## puzzle에 word1의 문자를 표기할때 뽑을 인덱스를 저장할 리스트
        location_y = [i for i in range(len(word2))] ## puzzle에 word2의 문자를 표기할때 뽑을 인덱스를 저장할 리스트
        location_x.remove(common_x) # 겹치는 문자를 제외하고 뽑으므로 삭제
        location_y.remove(common_y) # 겹치는 문자를 제외하고 뽑으므로 삭제
        
        #수정
        
        self.res_puzzle = [['#']*len(word1) for _ in range(len(word2))]
        
        i = 0
        while i < len(word1)-1:
                self.puzzle_board[common_y][location_x[i]] = '_'
                self.res_puzzle[common_y][location_x[i]] = word1[location_x[i]]
                i += 1
        #

        i = 0
        while i < (len(word1)-1)/2: # word1의 (len(word1)-1)/2 번 반복하며 puzzle_board에 문자를 표기
            random_index = random.randrange(0, len(location_x)) # random한 index 뽑기
            self.puzzle_board[common_y][location_x[random_index]] = word1[location_x[random_index]] # puzzle board에 문자 표기
            location_x.pop(random_index) # 뽑은 index는 다음번 random추출할때 제외하기 위해서 list에서 제거
            i += 1
        
        #수정
        i = 0
        while i < len(word2)-1:
                self.puzzle_board[location_y[i]][common_x] = '_'
                self.res_puzzle[location_y[i]][common_x] = word1[location_y[i]]
                i += 1
        #

        i = 0
        while i < (len(word2)-1)/2: #  word2의 (len(word1)-1)/2 번 반복하며 puzzle_board에 문자를 표기
            random_index = random.randrange(0, len(location_y)) # random한 index 뽑기
            self.puzzle_board[location_y[random_index]][common_x] = word2[location_y[random_index]]  # puzzle에 문자 표기
            location_y.pop(random_index) # 뽑은 index는 다음번 random 추출할때 제외하기 위해서 list에서 제거
            i += 1

        for i in range(len(self.puzzle_board)): # puzzle 출력부분
            print(self.puzzle_board[i])

#puzzle_make  = Puzzle_make()
#puzzle_make.make_puzzle()

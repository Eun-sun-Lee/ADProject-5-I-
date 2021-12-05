import copy
from puzzle_make import Puzzle_make
class Res_Check:
    def __init__(self, word):
    	 #정답 퍼즐을 저장
        self.word_res = word
        print(self.word_res)
    def cmp(self, inputs):
        res = True;
        #입력받은 퍼즐을 저장
        self.get_inputs = copy.deepcopy(inputs)
        print(self.get_inputs)
        #입력 퍼즐과 정답 퍼즐이 하나라도 다르면 False리턴
        for i in range(len(self.word_res)):
            for j in range(len(self.word_res[i])):
                if self.word_res[i]!=self.get_inputs[i]:
                    res=False
                    break
        return res

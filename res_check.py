import copy
from puzzle_make import Puzzle_make
class Res_Check:
    def __init__(self, word):
        self.word_res = word
        print(self.word_res)
    def cmp(self, inputs):
        res = True;
        self.get_inputs = copy.deepcopy(inputs)
        print(self.get_inputs)
        for i in range(len(self.word_res)):
            for j in range(len(self.word_res[i])):
                if self.word_res[i]!=self.get_inputs[i]:
                    res=False
                    break
        return res

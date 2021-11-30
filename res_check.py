class Res_Check:
    def __init__(self,words):
        self.word_res = words
        self.word_input = ""
    def cmp(self, inputs):
        self.word_input = inputs
        bool res=True;
        for i in range(self.word_input):
            if self.word_input[i]!=self.word_res[i]:
                res=False
                break
        return res

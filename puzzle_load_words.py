#두 단어 비교 후 낱말퍼즐이 형성될 수 있는지 확인
#겹치는 문자를 찾아서 낱말 퍼즐이 형성되는지 확인한다.
# 만약 겹치는 문자가 두 개 이상 ->  A 문자에서 가장 처음음위치를 선정하여 서로 겹치게 한다.


from word import Word

class Puzzle_load_words:
    def puzzle_word_generate(self, a, b):
        co1 = -1
        co2 = -1
        for i in a:
            for j in b:
                if i == j:
                    co1 = a.find(i) # a와 b가 겹치는 문자의 a에서의 index
                    co2 = b.find(j) # a와 b가 겹치는 문자의 b에서의 index
                    break
            if co1 != -1 and co2 != -1:
                break

        if co1 == -1:
            print('None')
            return None

        for i in range(len(b)): # b문자열 길이만큼 반복
            str = ''
            for j in range(len(a)): # a문자열 길이만큼 반복
                if i == co2: # 행 번호가 a와 b가 겹치는 문자의 b에서의 index와 같으면 그 행에는 a를 출력
                    str += a[j]
                elif j == co1: # 열 번호가 a와 b가 겹치는 문자의 a에서의 index와 같으면 그 열에는 b를 출력
                    str += b[i]
                else: # 그외는 .을 출력
                    str += '.'
            print(str)
        return (co1, co2)


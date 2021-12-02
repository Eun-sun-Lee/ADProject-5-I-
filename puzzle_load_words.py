#두 단어 비교 후 낱말퍼즐이 형성될 수 있는지 확인
#겹치는 문자를 찾아서 낱말 퍼즐이 형성되는지 확인한다.
# 만약 겹치는 문자가 두 개 이상 ->  A 문자에서 가장 처음 위치를 선정하여 서로 겹치게 한다.


from word import Word
class Puzzle_load_words:

    def __init__(self):
        word = Word('word.txt')
        a = word.randFromDB()
        b= word.randFromDB()
        if a == b:
            b = word.randFromDB()

    def puzzle_word_generate(a,b):
        co1 = 0
        co2 = 0
        for i in a:
            for j in b:
                if i == j and co2 == 0:
                    c = a.find(j)
                    co1 = 1
                    co2 = 1

        if co1 == 0:
            print('None')
            return
        print(c)
        count = 0
        total = 0
        for i in a:
            for j in b:
                if count == 0 and i == j:
                    count += 1
                    total += 1
            if count == 1 and total == 1:
                count = 0
                print(b)
            else:
                word = '.' * len(a)
                print(word[:c], i, word[c:])




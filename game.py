from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton,QMessageBox

import copy
from res_check import Res_Check
from puzzle_make import Puzzle_make
from puzzle_load_words import Puzzle_load_words
from word import Word

class Game(QWidget):
    def __init__(self, parent=None):
    	#GUI설정
        super().__init__(parent)
        self.gameLayout = QGridLayout()
        self.statusLayout = QGridLayout()
        self.mainLayout = QGridLayout()
        self.statustxt = QTextEdit()
        self.statusLayout.addWidget(self.statustxt)
        self.statustxt.setFixedSize(200,80)
        self.statustxt.setReadOnly(True)
        self.mainLayout.addLayout(self.statusLayout, 0, 1)
        self.rescheckButton = QToolButton()
        self.rescheckButton.setText('Res Check!')
        self.rescheckButton.clicked.connect(self.res_Check_Clicked)
        self.statusLayout.addWidget(self.rescheckButton, 0, 1)
        self.setLayout(self.mainLayout)
        self.setGeometry(100,200,300,400)
        self.setFixedSize(1000,800)
        self.setWindowTitle('CrossWord Game')
        self.startGame()
    def startGame(self):
    	#변수 초기화및 모듈초기화
        self.win = False
        self.Word = Word("word.txt")
        self.Puzzle_make = Puzzle_make()
        self.gameOver = False
        self.Puzzle_make.make_puzzle()
        self.statustxt.clear()
        self.gameSlot = copy.deepcopy(self.Puzzle_make.puzzle_board)
        print(self.Puzzle_make.puzzle_board)
        self.life = 10
        self.statustxt.setText("life : " + str(self.life))
        #puzzle_make에서 생성된 퍼즐을 GUI로 변환
        for i in range(len(self.Puzzle_make.puzzle_board)):
            for j in range(len(self.Puzzle_make.puzzle_board[i])):
                self.gameSlot[i][j]=QTextEdit()
                if self.Puzzle_make.puzzle_board[i][j]=='#':
                    self.gameSlot[i][j].setText("#")
                    self.gameSlot[i][j].setReadOnly(True)
                    self.gameSlot[i][j].setStyleSheet("background-color: black;")
                elif self.Puzzle_make.puzzle_board[i][j]!='_':
                    self.gameSlot[i][j].setText(self.Puzzle_make.puzzle_board[i][j])
                    self.gameSlot[i][j].setReadOnly(True)
                else:
                    self.gameSlot[i][j].setText("")
                    self.gameSlot[i][j].setReadOnly(False)
                font = self.gameSlot[i][j].font()
                font.setPointSize(font.pointSize()+30)
                self.gameSlot[i][j].setFont(font)
                self.gameSlot[i][j].setFixedHeight(100)
                self.gameSlot[i][j].setFont(font)
                self.gameSlot[i][j].setAlignment(Qt.AlignCenter)
        	#GUI 출력
                self.gameLayout.addWidget(self.gameSlot[i][j],i,j)
        self.mainLayout.addLayout(self.gameLayout, 0, 0)
        self.setLayout(self.mainLayout)
        #정답파일을 res_check로 전송 및 초기화
        self.res_check = Res_Check(self.Puzzle_make.res_puzzle)
        print(self.Puzzle_make.res_puzzle)
    def res_Check_Clicked(self):
    	#이미 승리하였다면 게임 초기화
        if self.win == True:
            self.startGame()
        #퍼즐판을 복사한 후 1문자로 이루어지지않는 텍스트위젯이 존재할경우 리턴
        self.nowslot = copy.deepcopy(self.Puzzle_make.puzzle_board)
        for i in range(len(self.gameSlot)):
            for j in range(len(self.gameSlot[i])):
                    self.nowslot[i][j]=self.gameSlot[i][j].toPlainText()
                    if len(self.nowslot[i][j])>2: #여러개의 문자가 들어왔을 때 에러 처리
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("알파벳 하나만 입력하세요.")
                        msg.setWindowTitle("---경고---")
                        msg.exec_()
                     #   self.statustxt.setText("알파벳 하나만 입력하세요.")
                        print("not 1 word")
                        return
                    elif len(self.nowslot[i][j])==0: #빈칸이 존재할 시 에러 처리
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("빈칸이 존재합니다. 모두 채워주세요.")
                        msg.setWindowTitle("---경고---")
                        msg.exec_()
                     #   self.statustxt.setText("빈칸이 존재합니다. 모두 채워주세요.")
                        print("exist 0 word")
                        return
        #목숨이 0이면 게임오버 출력, 게임 초기화
        if self.gameOver == True:
            print("GameOver")
            #self.statustxt.setText("Game Over\nStart new game")
            self.startGame()
            return
        #res_check.py를 통해 정답인지 체크
        success = self.res_check.cmp(self.nowslot)
        if success == False:
            #정답이 아니면 목숨-1
            self.life-=1
            print("-1 life")
            self.statustxt.setText("life : " + str(self.life))
            if(self.life==0):
            	#목숨이 0이라면 게임오버 true
                self.statustxt.setText("Game Over\nStart new game")
                self.gameOver=True
            return
        #승리했다면 승리문구 출력 및 win 변수 true
        self.statustxt.setText("You Win!\npush res check button to restart")
        self.win = True
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
    

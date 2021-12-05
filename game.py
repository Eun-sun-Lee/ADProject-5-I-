from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
import copy
from res_check import Res_Check
from puzzle_make import Puzzle_make
from puzzle_load_words import Puzzle_load_words
from word import Word

class Game(QWidget):
    def __init__(self, parent=None):
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
        self.win = False
        self.Word = Word("word.txt")
        self.Puzzle_make = Puzzle_make()
        self.gameOver = False
        self.Puzzle_make.make_puzzle()
        self.gameSlot = copy.deepcopy(self.Puzzle_make.puzzle_board)
        print(self.Puzzle_make.puzzle_board)
        self.life = 10
        self.statustxt.setText("life : " + str(self.life))
        for i in range(len(self.Puzzle_make.puzzle_board)):
            for j in range(len(self.Puzzle_make.puzzle_board[i])):
                self.gameSlot[i][j]=QTextEdit()
                if self.Puzzle_make.puzzle_board[i][j]=='#':
                    self.gameSlot[i][j].setText("#")
                    self.gameSlot[i][j].setReadOnly(True)
                elif self.Puzzle_make.puzzle_board[i][j]!='_':
                    self.gameSlot[i][j].setText(self.Puzzle_make.puzzle_board[i][j])
                    self.gameSlot[i][j].setReadOnly(True)
                else:
                    self.gameSlot[i][j].setText("")
                    self.gameSlot[i][j].setReadOnly(False)
                font = self.gameSlot[i][j].font()
                font.setPointSize(font.pointSize()+30)
                self.gameSlot[i][j].setFont(font)
                self.gameSlot[i][j].setFixedSize(100,100)
                self.gameSlot[i][j].setFont(font)
                self.gameSlot[i][j].setAlignment(Qt.AlignCenter)
                self.gameLayout.addWidget(self.gameSlot[i][j],i,j)
        self.mainLayout.addLayout(self.gameLayout, 0, 0)
        self.setLayout(self.mainLayout)
        self.res_check = Res_Check(self.Puzzle_make.res_puzzle)
        print(self.Puzzle_make.res_puzzle)
        self.statustxt.clear()
        self.win=False
    def res_Check_Clicked(self):
        if self.win == True:
            self.startGame()
        self.nowslot = copy.deepcopy(self.Puzzle_make.puzzle_board)
        for i in range(len(self.gameSlot)):
            for j in range(len(self.gameSlot[i])):
                    self.nowslot[i][j]=self.gameSlot[i][j].toPlainText()
                    if len(self.nowslot[i][j])!=1:
                        self.statustxt.setText("not one char")
                        print("not 1 word")
                        return

        if self.gameOver == True:
            print(GameOver)
            self.statustxt.setText("Game Over")
            pass
            print(a)

        success = self.res_check.cmp(self.nowslot)
        if success == False:
            self.life-=1
            print("-1 life")
            self.statustxt.setText("life : " + str(self.life))
            if(self.life==0):
                self.gameOver=True
            return

        self.statustxt.setText("You Win!\npush res check button to restart")
        self.win = True
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
    

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from functools import partial


class MyQpp(QWidget):
    # global bwidth, bheight, iwidth, iheight, rec
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        seats = [0 for _ in range(21)]
        for i in range(1, 20+1):
            seats[i] = QPushButton(f'번호 {i}', self)
            seats[i].resize(bwidth, bheight)
            seats[i].move(iwidth+(i-1)%6*bwidth + (i-1)%6//2*iwidth, 20+(i-1)//6*iheight)
            #partial : 함수와 argument를 넘기기 위해 사용
            seats[i].clicked.connect(partial(self.on_click, i))

        self.setWindowTitle('absolute 포지션')
        self.setGeometry(rec.width()//4, rec.height()//4, rec.width()//2, rec.height()//2)
        self.show()

    def on_click(self, i):
        print(i)

#main 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rec = app.desktop().geometry()      #모니터 크기 구하기
    bwidth = rec.width()//20; bheight = rec.height()//20;      #버튼의 크기
    iwidth = bwidth//2; iheight = bheight*1.8;     #버튼의 간격

    ex = MyQpp()
    sys.exit(app.exec_())


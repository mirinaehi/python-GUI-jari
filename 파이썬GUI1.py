import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont


class MyQpp(QWidget):
    # global bwidth, bheight, iwidth, iheight, rec
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        좌석 = [0 for _ in range(21)]
        for i in range(1, 6+1):
            좌석[i] = QPushButton(f'번호 {i}', self)
            좌석[i].resize(bwidth, bheight)
            좌석[i].move(i*bwidth + (i-1)//2*bwidth//3, 0)


        self.setWindowTitle('absolute 포지션')
        self.setGeometry(rec.width()//4, rec.height()//4, rec.width()//2, rec.height()//2)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    rec = app.desktop().geometry()      #모니터 크기 구하기
    bwidth = rec.width()//20; bheight = rec.height()//20;      #버튼의 크기
    iwidth = bwidth//2; iheight = bheight;     #버튼의 간격

    ex = MyQpp()
    sys.exit(app.exec_())


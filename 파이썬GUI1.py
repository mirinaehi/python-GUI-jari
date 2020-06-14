import sys, collections, random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from functools import partial


def PickToken():
    for i in range(1, 20+1):
        while True:
            temp = random.randint(1, 20)
            if 뽑기표[temp] ==0:
                뽑기표[temp] +=i
                break

#순서대로 뽑기(디버그용)
def PickTokenASC():
    for i in range(1, 20+1):
        뽑기표[i] = i

class MyQpp(QWidget):
    # global bwidth, bheight, iwidth, iheight, rec
    좌석 = [0 for _ in range(24+1)]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        for i in range(1, 18 + 1):
            self.좌석[i] = QPushButton(f'번호 {뽑기표[i]}', self)
            self.좌석[i].resize(bwidth, bheight)
            self.좌석[i].move(iwidth + (i - 1) % 6 * bwidth + (i - 1) % 6 // 2 * iwidth, 20 + (i - 1) // 6 * iheight)
            # partial : 함수와 argument를 넘기기 위해 사용
            self.좌석[i].clicked.connect(partial(self.on_click, i))

        for i in range(23, 24+1):
            self.좌석[i] = QPushButton(f'번호 {뽑기표[i-4]}', self)
            self.좌석[i].resize(bwidth, bheight)
            self.좌석[i].move(iwidth + (i - 1) % 6 * bwidth + (i - 1) % 6 // 2 * iwidth, 20 + (i - 1) // 6 * iheight)
            # partial : 함수와 argument를 넘기기 위해 사용
            self.좌석[i].clicked.connect(partial(self.on_click, i))

        self.setWindowTitle('absolute 포지션')
        self.setGeometry(rec.width() // 4, rec.height() // 4, rec.width() // 2, rec.height() // 2)
        self.show()

    def on_click(self, i):
        x축 = self.좌석[i].x()

        #맨 끝 위치 찾기
        for m in range(i, 24+1, 6):
            if 18<m<23:
                m -=6
                break

        for n in range(m, i, -6):
            for p in range(n-6, 0, -6):
                if self.좌석[p].isEnabled() and self.좌석[n].isEnabled():
                    self.좌석[n].move(x축, self.좌석[p].y())
                    break
                if self.좌석[n].isEnabled():
                    self.좌석[n].move(x축, 20)

        self.좌석[i].setEnabled(False)
        self.좌석[i].move(9999, 9999)


# main 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rec = app.desktop().geometry()  # 모니터 크기 구하기
    bwidth = rec.width() // 20;
    bheight = rec.height() // 20;  # 버튼의 크기
    iwidth = bwidth // 2;
    iheight = bheight * 1.8;  # 버튼의 간격
    뽑기표 = collections.Counter()

    PickToken()
    ex = MyQpp()
    sys.exit(app.exec_())

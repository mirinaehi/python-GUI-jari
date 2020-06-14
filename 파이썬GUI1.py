import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont


class MyQpp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)

        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('버튼1', self)
        btn1.move(50, 0)
        btn1.resize(btn1.sizeHint())  #버튼을 적절한 크기로 설정
        btn2 = QPushButton('버튼2', self)
        btn2.move(50, 100)
        btn2.resize(btn2.sizeHint())  # 버튼을 적절한 크기로 설정

        self.setWindowTitle('absolute 포지션')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyQpp()
    sys.exit(app.exec_())


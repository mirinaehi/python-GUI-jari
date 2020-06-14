import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyQpp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('첫번째 앱')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyQpp()
    sys.exit(app.exec_())


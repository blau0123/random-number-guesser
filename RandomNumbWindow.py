import sys
from PyQt5.QtWidgets import QApplication, QWidget

# create a movable, resizable window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(750, 750)
    w.move(300, 300)
    w.setWindowTitle('Random Number Guesser')
    w.show()

    sys.exit(app.exec_())

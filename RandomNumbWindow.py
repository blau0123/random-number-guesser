import sys
from PyQt5.QtWidgets import (QDesktopWidget, QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QIcon, QFont
# import RandomNumb.py


class RandomNumb(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('TimesNewRoman', 10))

        # creates a button that the user will use to submit guess
        submit = QPushButton('Submit', self)
        submit.setToolTip('This will submit your guess')
        submit.resize(submit.sizeHint())
        submit.move(350, 500)

        # creates the window properties
        self.resize(700, 700)
        self.center()

        self.setWindowTitle('Random Number Guesser')
        self.show()

    # centers the window in the middle of the screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# create a movable, resizable window
if __name__ == '__main__':
    # creates application object with command line args
    app = QApplication(sys.argv)
    rn = RandomNumb()
    sys.exit(app.exec_())

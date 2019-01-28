import sys
from PyQt5.QtWidgets import (QDesktopWidget, QWidget, QToolTip, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon, QFont
# import RandomNumb.py


class RandomNumb(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('TimesNewRoman', 10))

        # create grid layout for buttons
        grid = QGridLayout()
        # create a 2d arr that holds all widgets for each grid space
        btns = ['', '', '', '',
                '', '', '', '',
                '', '', '', '',
                '', '', '', '',
                'New Number', 'Submit', 'Quit']
        # sets a var that holds the (j, i) posits on btns 2d arr
        positions = [(i, j) for i in range(5) for j in range(4)]

        # for each posit in btns, insert the btn specified in btns
        for position, btn in zip(positions, btns):
            if btn == '':
                continue
            tempbut = QPushButton(btn)
            grid.addWidget(tempbut, *position)

        # creates the window properties
        # self.resize(700, 700)
        self.center()
        self.setLayout(grid)

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

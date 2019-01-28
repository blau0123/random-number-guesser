import sys
from PyQt5.QtWidgets import (QDesktopWidget, QWidget, QToolTip, QPushButton,
                             QLabel, QGridLayout, QApplication, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
# import RandomNumb.py


class RandomNumb(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('TimesNewRoman', 10))

        # create grid layout with all widgets
        grid = QGridLayout()

        # create three buttons
        submitbtn = QPushButton('Submit')
        newnumbbtn = QPushButton('New Number')
        quitbtn = QPushButton('Quit')
        grid.addWidget(newnumbbtn, 1, 0)
        grid.addWidget(submitbtn, 1, 1)
        grid.addWidget(quitbtn, 1, 2)

        # create a label that will give info to the user about the game & put in posit (0, 1(
        self.infolabel = QLabel('I have a number in my head. Try to guess it!', self)
        grid.addWidget(self.infolabel, 0, 1, Qt.AlignTop)

        newnumbbtn.clicked.connect(self.newNumbClicked)

        # creates the window properties
        self.center()
        self.setLayout(grid)

        self.setWindowTitle('Random Number Guesser')
        self.show()

    # if the user wants a new number
    def newNumbClicked(self):
        sender = self.sender()
        self.infolabel.setText('Fine, here\'s a new number. Now guess')

    # if the user wants to quit
    def quitClicked(self):
        # closes app

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

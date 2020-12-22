from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, QPushButton #TODO import additional Widget classes as desired
from PyQt5.QtCore import pyqtSlot, pyqtSignal

class ScoreBoard(QDockWidget):
    '''# base the score_board on a QDockWidget'''

    resetSignal = pyqtSignal(int) # signal sent when there is a new click location

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        #create a widget to hold other widgets
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        #create two labels which will be updated by signals
        self.label_clickLocation = QLabel("Click Location: ")
        self.label_timeRemaining = QLabel("Time remaining: ")
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.label_clickLocation)
        self.mainLayout.addWidget(self.label_timeRemaining)
        self.setWidget(self.mainWidget)

        self.passButton = QPushButton("Pass", self.mainWidget)
        self.mainLayout.addWidget(self.passButton)
        self.passButton.clicked.connect(self.passAction)

        self.resetButton = QPushButton("Reset", self.mainWidget)
        self.resetButton.clicked.connect(self.resetAction)

        self.mainLayout.addWidget(self.resetButton)

        self.show()

    def center(self):
        '''centers the window on the screen, you do not need to implement this method'''

    def make_connection(self, board):
        '''this handles a signal sent from the board class'''
        # when the clickLocationSignal is emitted in board the setClickLocation slot receives it
        board.clickLocationSignal.connect(self.setClickLocation)
        # when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
        board.updateTimerSignal.connect(self.setTimeRemaining)
        self.resetSignal.connect(board.resetSignal)

    @pyqtSlot(str) # checks to make sure that the following slot is receiving an argument of the type 'int'
    def setClickLocation(self, clickLoc):
        '''updates the label to show the click location'''
        self.label_clickLocation.setText("Click Location:" + clickLoc)
       # print('slot ' + clickLoc)

    @pyqtSlot(int)
    def setTimeRemaining(self, timeRemainng):
        '''updates the time remaining label to show the time remaining'''
        update = "Time Remaining:" + str(timeRemainng)
        self.label_timeRemaining.setText(update)
     #   print('slot '+update)
        # self.redraw()

    def passAction(self):
       print("Pass button clicked")
       self.resetSignal.emit(1)

    def resetAction(self):
       print("Reset button clicked")
       self.resetSignal.emit(0)

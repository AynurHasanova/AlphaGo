from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QMessageBox, QDialog, QTextEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from board import Board
from score_board import ScoreBoard

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def getBoard(self):
        return self.board

    def getScoreBoard(self):
        return self.scoreBoard

    def initUI(self):
        '''initiates application UI'''
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.RightDockWidgetArea, self.scoreBoard)
        self.scoreBoard.make_connection(self.board)


        # Open help document
        openAction = QAction(QIcon('help.png'), '&Help', self)
        openAction.setShortcut('Ctrl+H')
        openAction.setStatusTip('Open help')
        openAction.triggered.connect(self.openCall)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar with actions
        menubar = self.menuBar()
        # menu does not work on MacOS without setNativeMenuBar(False)
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        self.setMinimumSize(QSize(300, 100))
        self.resize(800, 800)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def openCall(self):
        userGuide = """Go("encircling game") is an abstract strategy board game for two players, in which the aim is to surround more territory than the opponent.The game was invented in China over 3, 000 years ago and is therefore believed to be the oldest board game continuously played today.It was considered one of the four essential arts of the cultured aristocratic Chinese scholars in antiquity.Despite its relatively simple rules, Go is very complex, even more so than chess.Computers have only recently been capable of beating human masters.Have a look at the following for more details: https: // deepmind.com / research / alphago / Movement: Black
        plays first, with black and white taking turns.A stone can be placed at any unoccupied intersection of the board with limited exceptions.
        
        Suicide Rule: You cannot place a stone which will immediately have no liberties.
        
        KO Rule(EternityRule): Previous game states are not allowed. Keep a list of previous game states which must be checked before stones are placed https://youtu.be/JWdgqV-8yVg?t=7
        m35s. """

        print('Help')
        helpWindow = QDialog(self)
        tb = QTextEdit(helpWindow)
        tb.resize(350, 250)
        tb.setReadOnly(True)
        tb.setText(userGuide)
        tb.setAlignment(Qt.AlignLeft)
        helpWindow.setWindowTitle("Help")
        helpWindow.setFixedHeight(260)
        helpWindow.setFixedWidth(360)
        helpWindow.show()

    def exitCall(self):
        print('Exiting game')

        buttonReply = QMessageBox.question(self, 'Exit Confirmation', "Exit Game?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()

    def clickMethod(self):
        print('PyQt')

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

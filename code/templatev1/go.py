from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QMessageBox, QDialog, QTextEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from board import Board
from score_board import ScoreBoard

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def get_board(self):
        return self.board

    def get_score_board(self):
        return self.scoreBoard

    def init_ui(self):
        """initiates application UI"""
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.RightDockWidgetArea, self.scoreBoard)
        self.scoreBoard.make_connection(self.board)

        # Open help document
        help_action = QAction(QIcon('help.png'), '&Help', self)
        help_action.setShortcut('Ctrl+H')
        help_action.setStatusTip('Open help')
        help_action.triggered.connect(self.help_call)

        # Create exit action
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.exit_call)

        # Create menu bar with actions
        menu_bar = self.menuBar()
        # menu does not work on MacOS without setNativeMenuBar(False)
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(help_action)
        file_menu.addAction(exit_action)

        self.resize(600, 600)
        #self.setFixedHeight(600)
        #self.setFixedWidth(600)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def help_call(self):
        user_guide = """Go("encircling game") is an abstract strategy board game for two players, in which the aim is to surround more territory than the opponent.The game was invented in China over 3, 000 years ago and is therefore believed to be the oldest board game continuously played today.It was considered one of the four essential arts of the cultured aristocratic Chinese scholars in antiquity.Despite its relatively simple rules, Go is very complex, even more so than chess.Computers have only recently been capable of beating human masters.Have a look at the following for more details: https: // deepmind.com / research / alphago / Movement: Black
        plays first, with black and white taking turns.A stone can be placed at any unoccupied intersection of the board with limited exceptions.
        
        Suicide Rule: You cannot place a stone which will immediately have no liberties.
        
        KO Rule(EternityRule): Previous game states are not allowed. Keep a list of previous game states which must be checked before stones are placed https://youtu.be/JWdgqV-8yVg?t=7
        m35s. """

        print('Help')
        help_window = QDialog(self)
        tb = QTextEdit(help_window)
        tb.resize(350, 250)
        tb.setReadOnly(True)
        tb.setText(user_guide)
        tb.setAlignment(Qt.AlignLeft)
        help_window.setWindowTitle("Help")
        help_window.setFixedHeight(260)
        help_window.setFixedWidth(360)
        help_window.show()

    def exit_call(self):
        print('Exiting game')

        exit_btn = QMessageBox.question(self, 'Exit Confirmation', "Exit Game?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if exit_btn == QMessageBox.Yes:
            self.close()

    @staticmethod
    def click_method():
        print('PyQt')

    def center(self):
        """centers the window on the screen"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

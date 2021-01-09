from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QTextEdit

# Main widgets
from widgets.board import Board
from widgets.main_layout import Ui_Main


class GoApp(Ui_Main, QtWidgets.QMainWindow):
    """
    This is the App's Main Widget. This will combine all of the apps
    properties together here. It will also be called in the entry point
    """

    # Default values
    board_width = 7

    def __init__(self, *args, **kwargs):
        super(GoApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)
        # self.center()

        self.moveCount = 0

        # Attach main Widgets
        self.board = Board(self, self.board_width)
        self.mainBoard_layout.addWidget(self.board)

        self.current_time = 10
        self.player_timer_dial.display(self.current_time)

        self.board.updateTimerSignal.connect(self.updateTimer)
        self.board.clickLocationSignal.connect(self.incrementMoves)
        self.board.nextPlayerColourSignal.connect(self.setNextPlayerColour)
        self.board.pointsSignal.connect(self.points)

        self.pass_btn.clicked.connect(self.changeTurns)
        self.reset_btn.clicked.connect(self.resetGame)

        self.actionAbout.triggered.connect(self.aboutCall)
        self.actionAbout.setShortcut('Ctrl+A')
        self.actionAbout.setIcon(QIcon('./assets/help.png'))

        self.actionExit.triggered.connect(self.exitCall)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setIcon(QIcon('./assets/exit.png'))
        self.actionHelp.triggered.connect(self.helpCall)
        self.actionHelp.setShortcut('Ctrl+H')
        self.actionHelp.setIcon(QIcon('./assets/help.png'))


    def incrementMoves(self, pos):
        """increments the move count"""
        self.moveCount += 1
        self.moves_count_label.setText(f"Moves: {self.moveCount}")
        self.current_move_label.setText(pos)

    def aboutCall(self):
        """about menu item"""
        _translate = QtCore.QCoreApplication.translate
        aboutText = _translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">AlphaGo</span><span style=\" font-size:12pt; vertical-align:sub;\">lite</span>v1.0.0</p></body></html>")

        print('About')
        help_window = QDialog(self)
        tb = QTextEdit(help_window)
        tb.resize(150, 150)
        tb.setReadOnly(True)
        tb.setText(aboutText)
        tb.setAlignment(Qt.AlignLeft)
        help_window.setWindowTitle("About")
        help_window.setFixedHeight(50)
        help_window.setFixedWidth(150)
        help_window.show()

    def exitCall(self):
        """exit menu item with confirmation"""
        print('Exiting game')
        button_reply = QtWidgets.QMessageBox.question(self, 'Exit Confirmation', "Exit Game?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            self.close()

    def helpCall(self):
        """helm menu item"""
        _translate = QtCore.QCoreApplication.translate
        helpText = _translate("Main", """
                        <html>
                            <head>
                            </head>
                            <body>
                            <h1>Go</h1>
                            <p>Overview</p>
                            <p>Go("encircling game") is an abstract strategy board game for two players, in which the aim is to surround more territory than the opponent. The game was invented in China over 3,000 years ago and is therefore believed to be the oldest board game continuously played today. It was considered one of the four essential arts of the cultured aristocratic Chinese scholars in antiquity. Despite its relatively simple rules, Go is very complex, even more so than chess. Computers have only recently been capable of beating human masters. 
                            Have a look at the following for more details: https://deepmind.com/research/alphago
                            <p>Movement</p>
                            <ul>
                            <li>
                            Two players: black and white taking turns
                            </li>
                            <li>
                            Black plays first. with black and white taking turns.A stone can be placed at any unoccupied intersection of the board with limited exceptions.
                            </li>
                            <li>
                            A stone can be placed at any unoccupied intersection of the board with limited exceptions.
                            </li>
                            </ul>
                            <p>Rules</p> 
                            <ul>
                            <li>
                            Suicide Rule: You cannot place a stone which will immediately have no liberties.
                            </li>
                            <li>
                            KO Rule(EternityRule): Previous game states are not allowed. Keep a list of previous game states which must be checked before stones are placed https://youtu.be/JWdgqV-8yVg?t=7m35s.
                            </li>
                            <ul>
                            </body>
                            </html>
                        """)

        print('Help')

        help_window = QDialog(self)
        tb = QTextEdit(help_window)
        tb.resize(400, 260)
        tb.setReadOnly(True)
        tb.setText(helpText)
        tb.setAlignment(Qt.AlignLeft)
        help_window.setWindowTitle("Help")
        help_window.setFixedHeight(260)
        help_window.setFixedWidth(400)
        help_window.show()

    def center(self):
        """ Centers the window on the screen """
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def updateTimer(self, timer):
        """updates the game timer with the provided timer"""
        self.current_time = timer
        self.player_timer_dial.display(self.current_time)

    def changeTurns(self):
        """gives turn to the other player"""
        self.board.game_logic.changePlayerTurn(True)
        self.setNextPlayerColour(self.board.game_logic.nextPlayerColour)

    def points(self):
        """calculates player points"""
        self.points_label.setText(self.board.game_logic.playerPoints)

    def resetGame(self):
        """resets the game board by clearing all states"""
        self.moveCount = -1
        return self.board.resetGame()

    def setNextPlayerColour(self, nextPlayer):
        """updates the label to show the next player name/colour"""
        print("Next Player: " + nextPlayer)
        self.current_player_label.setText(nextPlayer)
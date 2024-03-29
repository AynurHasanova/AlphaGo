from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QTextEdit, QMessageBox

# Main widgets
from widgets.board import Board
from widgets.main_layout import Ui_Main

import platform


class GoApp(Ui_Main, QtWidgets.QMainWindow):
    """
    This is the App's Main Widget. This will combine all of the apps
    properties together here. It will also be called in the entry point
    """

    def __init__(self, board_width, *args, **kwargs):
        super(GoApp, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # it is needed for MacOS, see https://stackoverflow.com/a/31028590
        if platform.system().lower() == "darwin":
            self.menubar.setNativeMenuBar(False)

        self.board_width = board_width
        self.moveCount = 0

        # Attach main Widgets
        self.board = Board(self, self.board_width)
        self.mainBoard_layout.addWidget(self.board)

        self.current_time = 100
        self.player_timer_dial.display(self.current_time)
        self.next_player_label.setText("Next Player: " + self.board.game_logic.currentPlayerColour)

        self.board.updateTimerSignal.connect(self.updateTimer)
        self.board.clickLocationSignal.connect(self.setMoves)
        self.board.nextPlayerColourSignal.connect(self.setNextPlayerColour)
        self.board.pointsSignal.connect(self.pointsAndTerritories)
        self.board.timeOutSignal.connect(self.timeOutPlayer)

        self.pass_btn.clicked.connect(self.changeTurns)
        self.undo_btn.clicked.connect(self.undoLastMove)
        self.reset_btn.clicked.connect(self.resetGame)

        self.actionAbout.triggered.connect(self.aboutCall)
        self.actionAbout.setShortcut('Ctrl+A')
        self.actionAbout.setIcon(QIcon('./assets/about.png'))

        self.saveGame_action.triggered.connect(self.board.saveGame)
        self.openGame_action.triggered.connect(self.board.openGame)

        self.actionExit.triggered.connect(self.exitCall)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setIcon(QIcon('./assets/exit.png'))
        self.actionHelp.triggered.connect(self.helpCall)
        self.actionHelp.setShortcut('Ctrl+H')
        self.actionHelp.setIcon(QIcon('./assets/help.png'))

    def setMoves(self, pos):
        """increments the total move count"""
        self.moveCount += 1

        self.moves_count_label.setText(f"Total Moves: {self.moveCount}")
        self.current_move_label.setText("Coordinates: " + pos)

    def aboutCall(self):
        """about menu item"""
        aboutText = "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">AlphaGo</span><span style=\" font-size:12pt; vertical-align:sub;\">lite</span>v1.0.0</p></body></html>"

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
        helpText = """
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
                        """

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
        button_reply = QtWidgets.QMessageBox.question(self, 'Pass Confirmation', "Are you sure to pass your turn?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            if self.board.game_logic.passTurn():
                self.showWinnerDialog(self.board.game_logic.currentPlayerColour, "two consecutive passes")
            # this may cause to a confusion, but game_logic.currentPlayerColour is always the next player
            # after the click on the board is finished
            self.setNextPlayerColour(self.board.game_logic.currentPlayerColour)
            self.board.resetTimer()

    def pointsAndTerritories(self):
        """calculates player points and territories"""
        self.black_points.setText("Black: " + str(self.board.game_logic.playerPoints[0]))
        self.white_points.setText("White: " + str(self.board.game_logic.playerPoints[1]))

        black_territories = 0
        white_territories = 0
        for row in self.board.game_logic.board_array:
            black_territories += row.count(self.board.BLACK)
            white_territories += row.count(self.board.WHITE)

        self.black_territories.setText("Black: " + str(black_territories))
        self.white_territories.setText("White: " + str(white_territories))

    def resetGame(self, hideDialog):
        """resets the game board by clearing all states"""
        self.moveCount = -1
        self.board.counter = 120

        # we don't need confirmation dialog to reset the board after a winner detected
        if hideDialog:
            self.board.resetGame()
        else:
            button_reply = QtWidgets.QMessageBox.question(self, 'Reset Confirmation', "Reset Game?",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
            if button_reply == QtWidgets.QMessageBox.Yes:
                self.board.resetTimer()
                self.board.resetGame()


    def undoLastMove(self):
        """undo the last move"""
        self.moveCount = -1
        self.board.counter = 120

        button_reply = QtWidgets.QMessageBox.question(self, 'Undo the Move', "Undo the Last Move?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            self.board.game_logic.undo()

    def setNextPlayerColour(self, nextPlayer):
        """updates the label to show the next player name/colour"""
        print("Next Player: " + nextPlayer)
        self.next_player_label.setText("Next Player: " + nextPlayer)

    def timeOutPlayer(self):
        """if the current players loses the game if the time passes"""
        self.showWinnerDialog(self.board.game_logic.currentPlayerColour, "2m timeout elapsed")

    def showWinnerDialog(self, player, reason):
        """shows a dialog box when a user loses the game"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Winner Detected")
        # msg.setInformativeText(f"Player {player} lost the game!")
        msg.setWindowTitle("Winner Detected")
        msg.setInformativeText(f"Player {player} lost the game!")
        msg.setDetailedText(f"Player {player} lost the game due to {reason}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.winnerConfirmation)

        retval = msg.exec_()
        print("Value of dialog box button:", retval)

    def winnerConfirmation(self, i):
        """resets the game after the OK button is pressed on the dialog box"""
        self.resetGame(True)
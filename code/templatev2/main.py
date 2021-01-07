from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

# Main widgets
from logic import GameLogic
from utils import BoardSize
from widgets.board import Board
from widgets.game_size import Ui_GameSize
from widgets.main_layout import Ui_Main


class GameSize(Ui_GameSize, QtWidgets.QDialog):
    statusSignal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(GameSize, self).__init__(*args, **kwargs)

        # Default Board Size
        self.boardSize = BoardSize.beginner.value
        self.setupUi(self)

        self.beginner_btn.clicked.connect(lambda x: self.setBoardSize(BoardSize.beginner))
        self.medium_btn.clicked.connect(lambda x: self.setBoardSize(BoardSize.medium))
        self.expert_btn.clicked.connect(lambda x: self.setBoardSize(BoardSize.expert))

        self.statusSignal.connect(lambda: print("Hello World"))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("Hello World")

    def accept(self):
        print('Opening the Main App with', self.boardSize, 'size')
        self.statusSignal.emit()
        self.close()

    def reject(self):
        print("Hello")
        self.close()

    def setBoardSize(self, type: BoardSize):
        self.boardSize = type.value


class GoApp(Ui_Main, QtWidgets.QMainWindow):
    """
    This is the App's Main Widget. This will combine all of the apps
    properties together here. It will also be called in the entry point

    """

    # TODO All the App's signals
    statusBarWrite = QtCore.pyqtSignal(str)
    increaseMove = QtCore.pyqtSignal(int)
    passAction = QtCore.pyqtSignal(int)

    # TODO Default values
    board_width = 7

    def __init__(self, *args, **kwargs):
        super(GoApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)
        # self.center()

        self.moveCount = 0

        # TODO Attach main Widgets
        self.board = Board(self, self.board_width)
        self.mainBoard_layout.addWidget(self.board)

        self.current_time = 10
        self.player_timer_dial.display(self.current_time)

        self.board.updateTimerSignal.connect(self.updateTimer)
        self.board.clickLocationSignal.connect(self.increment_moves)
        self.board.nextPlayerColourSignal.connect(self.setNextPlayerColour)

        self.pass_btn.clicked.connect(self.flipPlayer)
        self.reset_btn.clicked.connect(self.board.resetGame)

    def increment_moves(self, pos):
        self.moveCount += 1
        self.moves_count_label.setText(f"Moves: {self.moveCount}")
        self.current_move_label.setText(pos)

    def exitCall(self):
        print('Exiting game')
        button_reply = QtWidgets.QMessageBox.question(self, 'Exit Confirmation', "Exit Game?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            self.close()

    def center(self):
        """ Centers the window on the screen """
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def updateTimer(self, timer):
        self.current_time = timer
        self.player_timer_dial.display(self.current_time)

    def flipPlayer(self):
        print("Pass signal received")
        self.board.game_logic.change_player_turn(True)
        # self.next_player_colour_signal.emit(self.game_logic.next_player_colour)
        self.setNextPlayerColour(self.board.game_logic.next_player_colour)

    def setNextPlayerColour(self, nextPlayer):
        """updates the label to show the next player name/colour"""
        print("Next Player: " + nextPlayer)
        self.current_player_label.setText(nextPlayer)
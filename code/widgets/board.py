import os
import pickle
from copy import deepcopy
from pathlib import Path

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QPoint
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QFrame, QMessageBox

from logic import GameLogic
from utils import Color

BASE_PATH = Path(__file__).resolve().parent.parent


class Board(QFrame):
    # Board default values
    # This is size of each cells of squares on the Go Board
    SQUARE_SIZE = 50
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    # TODO set the board width and height to be square
    timerSpeed = 1000  # the timer updates every 1 second
    counter = 100  # the number the counter will count down from

    TURNS = (
        BLACK,
        WHITE,
    )

    # All the App's signals
    pointsSignal = pyqtSignal(tuple)            # used to send pointsAndTerritories to the score_board
    updateTimerSignal = pyqtSignal(int)         # signal sent when timer is updated
    clickLocationSignal = pyqtSignal(str)       # signal sent when there is a new click location
    nextPlayerColourSignal = pyqtSignal(str)    # signal sent with the next player name
    updateBoardSignal = pyqtSignal()            # signal sent to to update the board anytime
    gameStartedSignal = pyqtSignal(bool)

    def __init__(self, parent, board_width):
        super().__init__(parent)
        self.init_board(board_width)

        # This will be used for saving the game to a file
        self.isSaved = False
        self.path = None

    def init_board(self, board_width):
        # start with a black player
        self.turn = self.BLACK

        print(Color.WARNING + Color.BOLD, Path(__file__).resolve().parent.parent, Color.ENDLINE)

        self.updateBoardSignal.connect(self.update)
        self.gameStartedSignal.connect(self.setGameStarted)

        # create a timer for the game
        self.timer = QBasicTimer()
        self.isStarted = False
        self.board_width = self.board_height = board_width

        self.board_array = [[0 for _ in range(board_width)] for _ in range(board_width)]
        self.game_logic = GameLogic(self.board_array, self.updateBoardSignal)

        # self.setBoardCursor()

        self.printBoardArray()
        self.clearTimer()                       # start the game which will start the timer

    def printBoardArray(self):
        """ prints the board_array in an attractive way """
        print("board_array:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.game_logic.board_array]))

    # TODO Add Animated and Custom Cursor
    def setBoardCursor(self):
        self.cursor_pix = QtGui.QBitmap(os.path.join(BASE_PATH, 'assets/help.png'))
        self.current_curs = QtGui.QCursor(self.cursor_pix)
        self.setCursor(self.current_curs)

    def squareWidth(self):
        """ returns the width of one square in the board """
        return self.SQUARE_SIZE

    def setGameStarted(self, state):
        self.isStarted = state
        if state:
            self.timer.stop()

    def squareHeight(self):
        """ returns the height of one square of the board """
        return self.SQUARE_SIZE

    def clearTimer(self):
        """ Starts game """
        # set the boolean which determines if the game has started to TRUE
        self.isStarted = True

        # start the timer with the correct speed
        self.timer.start(self.timerSpeed, self)
        print("start () - timer is started")

    def resetTimer(self):
        self.counter = 100

        # Here the timer is recreated so it will reset the timer to abs. zero
        self.clearTimer()
        self.updateTimerSignal.emit(self.counter)

    def timerEvent(self, event):
        """ This event is automatically called when the timer is updated. based on the timerSpeed variable """
        # TODO adapter this code to handle your timers
        if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
            if Board.counter == 0:
                print("Game over")
            self.counter -= 1
            self.updateTimerSignal.emit(self.counter)
        else:
            super(Board, self).timerEvent(event)  # if we do not handle an event we should pass it to the super
            # class for handling other wise pass it to the super class for handling

    def paintEvent(self, event):
        """ Paints the board and the pieces of the game """
        painter = QPainter(self)
        self.drawSquares(painter)
        self.drawPieces(painter)

    def roundUp(self, i, v):
        """ Rounds up a number (i) to nearest multiple of the square size (v) """
        return round(i / v) * v

    def mousePressEvent(self, event):
        """ This event is automatically called when the mouse is pressed """
        col = int(self.roundUp(event.x(), self.SQUARE_SIZE) / self.squareWidth())
        row = int(self.roundUp(event.y(), self.SQUARE_SIZE) / self.squareHeight())

        clickLoc = f'{chr(65 + col - 1)}{row}'  # map to letter-number format

        if (0 < row < 8) and (0 < col < 8):
            tryValue = self.game_logic.tryMove(row - 1, col - 1)
            if tryValue == 0:
                # if tryMove succeeds then update the next player colour
                self.nextPlayerColourSignal.emit(self.game_logic.currentPlayerColour)
            elif tryValue == 1:
                self.showMoveResult("({}, {}) is not free".format(row - 1, col - 1))
                print("tryMove({}, {}) failed".format(row - 1, col - 1))
            elif tryValue == 2:
                self.showMoveResult("(Move to {}, {}) is suicidal".format(row - 1, col - 1))
            elif tryValue == 3:
                self.showMoveResult("Move to ({}, {}) is KO".format(row - 1, col - 1))

        else:
            print("Out-of-band Calculated row: {}, col: {}", row, col)

        self.clickLocationSignal.emit(clickLoc)
        self.pointsSignal.emit(self.game_logic.playerPoints)
        self.resetTimer()
        self.updateBoardSignal.emit()

    def saveGame(self):
        if not self.isSaved:
            # Get the file name
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                "All files",
                                                                QtCore.QDir.homePath(),
                                                                "AlphaGo Game (*.alg);; Pickle File (*.pickle)")
            # If the user cancelled the dialog
            if not fileName:
                QtWidgets.QMessageBox.warning(self, 'File Not given', 'No file was provided')
            else:
                # Copy the exact state of the state at that moment
                state = deepcopy(self.game_logic.state)
                try:
                    with open(fileName, 'wb') as fp:
                        pickle.dump(state, fp)
                    self.isSaved = True
                    self.path = fileName
                    QtWidgets.QMessageBox.information(self, 'Successful', 'Your Game is now saved')
                except OSError:
                    QtWidgets.QMessageBox.critical(self, 'Error', 'An error occurred')

    def resetGame(self):
        """ Clears pieces from the board """
        self.init_board(self.board_width)
        self.clickLocationSignal.emit("")
        self.nextPlayerColourSignal.emit("Black")
        self.pointsSignal.emit(self.game_logic.playerPoints)
        self.updateTimerSignal.emit(self.counter)
        # We need to call update to trigger paintEvent
        self.updateBoardSignal.emit()

    def drawSquares(self, painter):
        """ This method draws the board based on the given dimensions """
        # Draw horizontal lines
        for i in zip([_ for _ in range(1, self.board_width + 1)], [chr(_) for _ in range(65, 1000)]):
            painter.drawText(self.SQUARE_SIZE * i[0] - 3, self.SQUARE_SIZE - 20, i[1])

        for i in range(1, self.board_width + 1):
            painter.drawLine(self.SQUARE_SIZE, self.SQUARE_SIZE * i, self.board_width * self.SQUARE_SIZE,
                             self.SQUARE_SIZE * i)

        for i in range(1, self.board_width + 1):
            painter.drawText(self.SQUARE_SIZE - 30, self.SQUARE_SIZE * i + 5, str(i))

        # Draw vertical lines
        for i in range(1, self.board_width + 1):
            painter.drawLine(self.SQUARE_SIZE * i, self.SQUARE_SIZE, self.SQUARE_SIZE * i,
                             self.board_width * self.SQUARE_SIZE)

    def drawPieces(self, painter):
        """ This draws the game pieces on the board """
        for row in range(0, len(self.game_logic.board_array)):
            for col in range(0, len(self.game_logic.board_array[0])):
                colTransformation = (col + 1) * self.squareWidth()
                rowTransformation = (row + 1) * self.squareHeight()

                # Todo choose your colour and set the painter brush to the correct colour
                if self.game_logic.board_array[row][col] == 1:
                    colour = Qt.black
                elif self.game_logic.board_array[row][col] == 2:
                    colour = Qt.white
                else:
                    continue

                painter.save()
                painter.translate(colTransformation, rowTransformation)
                painter.setBrush(colour)

                # draw some the pieces as elipses
                radius1 = (self.squareWidth() - 2) / 4
                radius2 = (self.squareHeight() - 2) / 4
                center = QPoint(row, col)
                painter.drawEllipse(center, radius1, radius2)
                painter.restore()

    def showMoveResult(self, moveResult):
        """shows a dialog that displayes how the last move when if it fails"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Unsuccessful Move")
        msg.setWindowTitle("Unsuccessful Move")
        msg.setInformativeText(moveResult)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()

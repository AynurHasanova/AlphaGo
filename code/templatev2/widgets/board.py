from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QPoint, pyqtSlot
from PyQt5.QtGui import QPainter

from logic import GameLogic
from utils import Player


class Board(QFrame):
    # TODO Board default values

    # This is size of each cells of squares on the Go Board
    SQUARE_SIZE = 50
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    # TODO set the board width and height to be square
    timerSpeed = 1000  # the timer updates every 1 second
    counter = 10  # the number the counter will count down from

    TURNS = (
        BLACK,
        WHITE,
    )

    # TODO Main Signals
    points_signal = pyqtSignal(str)  # used to send points to the score_board
    updateTimerSignal = pyqtSignal(int)  # signal sent when timer is updated
    clickLocationSignal = pyqtSignal(str)  # signal sent when there is a new click location
    nextPlayerColourSignal = pyqtSignal(str)  # signal sent with the next player name

    def __init__(self, parent, board_width):
        super().__init__(parent)
        self.init_board(board_width)


    def init_board(self, board_width):
        # The First player is always a black
        self.turn = self.BLACK

        # create a timer for the game
        self.timer = QBasicTimer()
        self.isStarted = False

        self.board_width = self.board_height = board_width
        self.board_array = [[0 for _ in range(board_width)] for _ in range(board_width)]
        self.game_logic = GameLogic(self.board_array)

        self.printBoardArray()  # TODO - uncomment this method after create the array above
        # self.game_logic = game_logic(self.boardArray)

        # TODO - Is this necessary, I thought scores in Go is computed after the game is over
        # Player scores by core
        # self._score = {
        #     self.BLACK: 0,
        #     self.WHITE: 0,
        # }

        self.start()  # start the game which will start the timer
        # TODO - create a 2d int/Piece array to store the state of the game

    def printBoardArray(self):
        """ prints the board_array in an attractive way """
        print("board_array:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board_array]))

    def mousePosToColRow(self, event):
        """ convert the mouse click event to a row and column """
        # print("mousePosToColRow: " + self.squareWidth() / event.pos().x())

    def squareWidth(self):
        """ returns the width of one square in the board """
        return self.SQUARE_SIZE
        # return self.contentsRect().width() / self.boardWidth

    def squareHeight(self):
        """ returns the height of one square of the board """
        return self.SQUARE_SIZE
        # return self.contentsRect().height() / self.boardHeight

    def start(self):
        """ Starts game """
        # set the boolean which determines if the game has started to TRUE
        self.isStarted = True
        #self.resetGame()

        # start the timer with the correct speed
        self.timer.start(self.timerSpeed, self)
        print("start () - timer is started")

    def timerEvent(self, event):
        """ This event is automatically called when the timer is updated. based on the timerSpeed variable """
        # TODO adapter this code to handle your timers
        if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
            if Board.counter == 0:
                print("Game over")
            self.counter -= 1
            #  print('timerEvent()', self.counter)
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

        # print("mousePressEvent() - "+clickLoc)
        # TODO you could call some game logic here

        col = int(self.roundUp(event.x(), self.SQUARE_SIZE) / self.squareWidth())
        row = int(self.roundUp(event.y(), self.SQUARE_SIZE) / self.squareHeight())

        click_loc = f'{chr(65 + col - 1)}{row}'

        # clickLoc = "click loc: [" + str(event.x()) + "," + str(event.y()) + "] -> " + str(row) + ", " + str(col)
        self.clickLocationSignal.emit(click_loc)
        self.nextPlayerColourSignal.emit(self.game_logic.next_player_colour)

        if (0 < row < 8) and (0 < col < 8):
            if not self.game_logic.try_move(row - 1, col - 1):
                print("try_move({}, {}) failed".format(row - 1, col - 1))
        else:
            print("Out-of-band Calculated row: {}, col: {}", row, col)
        self.update()

        self.points_signal.emit(self.game_logic.player_points)

        # change the value depending on the player colour

    def resetGame(self):
        """ Clears pieces from the board """
        # TODO write code to reset game
        print("Reset signal received")
        self.init_board(self.board_width)
        # We need to call update to trigger paintEvent
        self.update()
        self.nextPlayerColourSignal.emit("BLACK")

    def tryMove(self, newX, newY):
        """ Tries to move a piece """
        pass

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
        # FIXME - This variable wasn't used
        colour = Qt.transparent  # empty square could be modeled with transparent pieces
        for row in range(0, len(self.board_array)):
            for col in range(0, len(self.board_array[0])):
                colTransformation = (col + 1) * self.squareWidth()
                rowTransformation = (row + 1) * self.squareHeight()

                # Todo choose your colour and set the painter brush to the correct colour
                if self.board_array[row][col] == 1:
                    colour = Qt.black
                elif self.board_array[row][col] == 2:
                    colour = Qt.white
                else:
                    continue

                painter.save()
                painter.translate(colTransformation, rowTransformation)
                painter.setBrush(colour)

                # Todo draw some the pieces as elipses
                radius1 = (self.squareWidth() - 2) / 4
                radius2 = (self.squareHeight() - 2) / 4
                print("self.squareWidth(): {}, self.squareHeight(): {}, radius1: {}, radius2: {}".format(
                    self.squareWidth(), self.squareHeight(), radius1, radius2))
                center = QPoint(row, col)
                print(center)
                painter.drawEllipse(center, radius1, radius2)
                painter.restore()

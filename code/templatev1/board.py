from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QPoint, pyqtSlot
from PyQt5.QtGui import QPainter
from piece import Piece
from game_logic import GameLogic

class Board(QFrame):  # base the board on a QFrame widget
    BLACK = 1
    WHITE = 2
    EMPTY = 0

    SQUARE_SIZE = 50

    TURNS = (
        BLACK,
        WHITE,
    )

    updateTimerSignal = pyqtSignal(int) # signal sent when timer is updated
    clickLocationSignal = pyqtSignal(str) # signal sent when there is a new click location

    # TODO set the board width and height to be square
    boardWidth  = 7     # board is 0 squares wide # TODO this needs updating
    boardHeight = 7     #
    timerSpeed  = 1     # the timer updates ever 1 second
    counter     = 10    # the number the counter will count down from

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        '''initiates board'''
        self.timer = QBasicTimer()  # create a timer for the game
        self.isStarted = False      # game is not currently started


        # TODO - create a 2d int/Piece array to store the state of the game
        self.boardArray = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]
                           ]
        self.printBoardArray()    # TODO - uncomment this method after create the array above

        self.gameLogic = GameLogic(self.boardArray)

        self.turn = self.BLACK     # blacks start first

        # Player scores by core
        self._score = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Keep the game history
        self._history = []

        self.start()                # start the game which will start the timer


    def printBoardArray(self):
        '''prints the boardArray in an attractive way'''
        print("boardArray:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.boardArray]))

    def mousePosToColRow(self, event):
        '''convert the mouse click event to a row and column'''
        # print("mousePosToColRow: " + self.squareWidth() / event.pos().x())

    def squareWidth(self):
        '''returns the width of one square in the board'''
        return self.SQUARE_SIZE
        #return self.contentsRect().width() / self.boardWidth

    def squareHeight(self):
        '''returns the height of one square of the board'''
        return self.SQUARE_SIZE
        #return self.contentsRect().height() / self.boardHeight

    def start(self):
        '''starts game'''
        self.isStarted = True                       # set the boolean which determines if the game has started to TRUE
        self.resetGame()                            # reset the game
        self.timer.start(self.timerSpeed, self)     # start the timer with the correct speed
        print("start () - timer is started")

    def timerEvent(self, event):
        '''this event is automatically called when the timer is updated. based on the timerSpeed variable '''
        # TODO adapter this code to handle your timers
        if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
            if Board.counter == 0:
                print("Game over")
            self.counter -= 1
          #  print('timerEvent()', self.counter)
            self.updateTimerSignal.emit(self.counter)
        else:
            super(Board, self).timerEvent(event)      # if we do not handle an event we should pass it to the super
                                                        # class for handelingother wise pass it to the super class for handling

    def paintEvent(self, event):
        '''paints the board and the pieces of the game'''
        painter = QPainter(self)
        self.drawSquares(painter)
        self.drawPieces(painter)

    def roundUp(self, i, v):
        '''Rounds up a number (i) to nearest multiple of the square size (v)'''
        return round(i / v) * v

    def mousePressEvent(self, event):
        '''this event is automatically called when the mouse is pressed'''
        #print("mousePressEvent() - "+clickLoc)
        # TODO you could call some game logic here

        col = (int)(self.roundUp(event.x(), self.SQUARE_SIZE) / self.squareWidth())
        row = (int)(self.roundUp(event.y(), self.SQUARE_SIZE) / self.squareHeight())

        clickLoc = "click loc: ["+str(event.x())+","+str(event.y())+"] -> " + str(row) + ", " + str(col)
        self.clickLocationSignal.emit(clickLoc)

        if ( row > 0 and row < 8 ) and ( col > 0 and col < 8 ):
            self.gameLogic.move(row, col)
        else:
            print("Out-of-band Calculated row: {}, col: {}", row, col)

        # change the value depending on the player colour

    def resetGame(self):
        '''clears pieces from the board'''
        # TODO write code to reset game

    def tryMove(self, newX, newY):
        '''tries to move a piece'''
        pass

    def drawSquares(self, painter):
        # Draw horizontal lines
        # Draw vertical lines
        for i in range(1, self.boardWidth + 1):
            painter.drawLine(self.SQUARE_SIZE, self.SQUARE_SIZE * i, self.boardWidth * self.SQUARE_SIZE, self.SQUARE_SIZE * i)

        # Draw vertical lines
        for i in range(1, self.boardWidth + 1):
            painter.drawLine(self.SQUARE_SIZE * i, self.SQUARE_SIZE, self.SQUARE_SIZE * i, self.boardWidth * self.SQUARE_SIZE)

    def drawPieces(self, painter):
        '''draw the prices on the board'''
        colour = Qt.transparent # empty square could be modeled with transparent pieces
        for row in range(0, len(self.boardArray)):
            for col in range(0, len(self.boardArray[0])):
                colTransformation = (col + 1) * self.squareWidth()
                rowTransformation = (row + 1) * self.squareHeight()

                #Todo choose your colour and set the painter brush to the correct colour
                if self.boardArray[row][col] == 1:
                    colour = Qt.black
                elif self.boardArray[row][col] == 2:
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

    @pyqtSlot(int)
    def resetSignal(self, action):
        '''receives signal from score board'''
        update = "Received action :" + str(action)
        if action == 0:
            print("Reset signal received")
        else:
            print("Pass signal received")
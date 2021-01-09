from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QPoint, pyqtSlot
from PyQt5.QtGui import QPainter
from game_logic import GameLogic


class Board(QFrame):  # base the board on a QFrame widget
    SQUARE_SIZE = 50

    points_signal = pyqtSignal(str)  # used to send pointsAndTerritories to the score_board
    update_timer_signal = pyqtSignal(int) # signal sent when timer is updated
    click_location_signal = pyqtSignal(str) # signal sent when there is a new click location
    next_player_colour_signal = pyqtSignal(str)  # signal sent with the next player name

    board_width = 7     # 7x7 board
    board_height = 7    # 7x7 board
    timer_speed = 1     # the timer updates ever 1 second
    counter = 10    # the number the counter will count down from

    def __init__(self, parent):
        super().__init__(parent)
        self.init_board()

    def init_board(self):
        """initiates board"""
        self.timer = QBasicTimer()   # create a timer for the game
        self.is_started = False      # game is not currently started

        self.board_array = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.print_board_array()
        self.game_logic = GameLogic(self.board_array)
        self.start()                # start the game which will start the timer

    def print_board_array(self):
        """prints the board_array in an attractive way"""
        print("board_array:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board_array]))

    def mouse_pos_to_col_row(self, event):
        """convert the mouse click event to a row and column"""
        # print("mouse_pos_to_col_row: " + self.square_width() / event.pos().x())

    def square_width(self):
        """returns the width of one square in the board"""
        return self.SQUARE_SIZE
        #return self.contentsRect().width() / self.board_width

    def square_height(self):
        """returns the height of one square of the board"""
        return self.SQUARE_SIZE
        #return self.contentsRect().height() / self.board_height

    def start(self):
        """starts game"""
        self.is_started = True                     # set the boolean which determines if the game has started to TRUE
        self.timer.start(self.timer_speed, self)   # start the timer with the correct speed
        print("start () - timer is started")

    def timerEvent(self, event):
        """this event is automatically called when the timer is updated. based on the timer_speed variable """
        # TODO adapter this code to handle your timers
        if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
            if Board.counter == 0:
                print("Game over")
            self.counter -= 1
            # print('timerEvent()', self.counter)
            self.update_timer_signal.emit(self.counter)
        else:
            super(Board, self).timerEvent(event)      # if we do not handle an event we should pass it to the super
                                                      # class for handelingother wise pass it to the super class for handling

    def paintEvent(self, event):
        """paints the board and the pieces of the game"""
        painter = QPainter(self)
        self.draw_squares(painter)
        self.draw_pieces(painter)

    @staticmethod
    def roundup(i, v):
        """Rounds up a number (i) to nearest multiple of the square size (v)"""
        return round(i / v) * v

    def mousePressEvent(self, event):
        """this event is automatically called when the mouse is pressed"""
        #print("mousePressEvent() - "+click_loc)
        # TODO you could call some game logic here

        col = int(self.roundup(event.x(), self.SQUARE_SIZE) / self.square_width())
        row = int(self.roundup(event.y(), self.SQUARE_SIZE) / self.square_height())

        click_loc = "["+str(row) + ", " + str(col) + "]"
        self.click_location_signal.emit(click_loc)
        self.next_player_colour_signal.emit(self.game_logic.currentPlayerColour)

        if (0 < row < 8) and (0 < col < 8):
            if not self.game_logic.tryMove(row - 1, col - 1):
                print("tryMove({}, {}) failed".format(row-1, col-1))
        else:
            print("Out-of-band Calculated row: {}, col: {}", row, col)

        self.points_signal.emit(self.game_logic.playerPoints)

    def draw_squares(self, painter):
        # Draw horizontal lines
        # Draw vertical lines
        for i in range(1, self.board_width + 1):
            painter.drawLine(self.SQUARE_SIZE, self.SQUARE_SIZE * i, self.board_width * self.SQUARE_SIZE, self.SQUARE_SIZE * i)

        # Draw vertical lines
        for i in range(1, self.board_width + 1):
            painter.drawLine(self.SQUARE_SIZE * i, self.SQUARE_SIZE, self.SQUARE_SIZE * i, self.board_width * self.SQUARE_SIZE)

    def draw_pieces(self, painter):
        """draw the prices/stones on the board"""
        for row in range(0, len(self.board_array)):
            for col in range(0, len(self.board_array[0])):
                col_transformation = (col + 1) * self.square_width()
                row_transformation = (row + 1) * self.square_height()

                if self.board_array[row][col] == 1:
                    colour = Qt.black
                elif self.board_array[row][col] == 2:
                    colour = Qt.white
                else:
                    continue

                painter.save()
                painter.translate(col_transformation, row_transformation)
                painter.setBrush(colour)

                radius1 = (self.square_width() - 2) / 4
                radius2 = (self.square_height() - 2) / 4
                center = QPoint(row, col)
                painter.drawEllipse(center, radius1, radius2)
                painter.restore()

    @pyqtSlot(int)
    def reset_signal(self, action):
        """receives signal from score board and resets the board or passes the turn"""
        update = "Received action :" + str(action)
        if action == 0:
            print("Reset signal received")
            self.init_board()
            # We need to call update to trigger paintEvent
            self.update()
            self.next_player_colour_signal.emit("BLACK")
        else:
            print("Pass signal received")
            self.game_logic.changePlayerTurn(True)
            self.next_player_colour_signal.emit(self.game_logic.currentPlayerColour)

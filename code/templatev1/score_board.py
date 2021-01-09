from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class ScoreBoard(QDockWidget):
    """# base the score_board on a QDockWidget"""

    resetSignal = pyqtSignal(int) # signal sent when there is a new click location

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """initiates ScoreBoard UI"""
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        # create a widget to hold other widgets
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()

        #create two labels which will be updated by signals
        self.label_clickLocation = QLabel("Click Location: ")
        self.label_nextPlayer = QLabel("Next Player: ")
        self.label_player_points = QLabel("Player Points: ")
        self.label_timeRemaining = QLabel("Time Remaining: ")
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.addWidget(self.label_clickLocation)
        self.main_layout.addWidget(self.label_nextPlayer)
        self.main_layout.addWidget(self.label_player_points)
        self.main_layout.addWidget(self.label_timeRemaining)
        self.setWidget(self.main_widget)

        self.pass_button = QPushButton("Pass", self.main_widget)
        self.main_layout.addWidget(self.pass_button)
        self.pass_button.clicked.connect(self.pass_action)

        self.reset_button = QPushButton("Reset", self.main_widget)
        self.reset_button.clicked.connect(self.reset_action)

        self.main_layout.addWidget(self.reset_button)

        # self.setFixedHeight(600)
        # self.setFixedWidth(300)

        self.show()

    def center(self):
        """centers the window on the screen, you do not need to implement this method"""

    def make_connection(self, board):
        """this handles a signal sent from the board class"""
        # when the click_location_signal is emitted in board the set_click_location slot receives it
        board.click_location_signal.connect(self.set_click_location)
        # when the click_location_signal is emitted in board the set_click_location slot receives it
        board.next_player_colour_signal.connect(self.set_next_player_colour)
        # get pointsAndTerritories from board.py
        board.pointsSignal.connect(self.set_player_points)
        # when the update_timer_signal is emitted in the board the set_time_remaining slot receives it
        board.update_timer_signal.connect(self.set_time_remaining)
        self.resetSignal.connect(board.reset_signal)

    @pyqtSlot(str) # checks to make sure that the following slot is receiving an argument of the type 'int'
    def set_click_location(self, click_loc):
        """updates the label to show the latest click location"""
        self.label_clickLocation.setText("Location: " + click_loc)
        # print('slot ' + click_loc)

    @pyqtSlot(str)
    def set_next_player_colour(self, next_player):
        """updates the label to show the next player name/colour"""
        self.label_nextPlayer.setText("Next Player: " + next_player)

    @pyqtSlot(str)
    def set_player_points(self, points):
        self.label_player_points.setText("Points: " + points)

    @pyqtSlot(int)
    def set_time_remaining(self, time_remainng):
        """updates the time remaining label to show the time remaining"""
        update = "Time Remaining:" + str(time_remainng)
        self.label_timeRemaining.setText(update)
        # print('slot '+update)
        # self.redraw()

    def pass_action(self):
        print("Pass button clicked")
        self.resetSignal.emit(1)

    def reset_action(self):
        print("Reset button clicked")
        self.resetSignal.emit(0)

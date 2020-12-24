from collections import namedtuple
from copy import copy


class GameLogic:
    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game

    BLACK = 1
    WHITE = 2
    EMPTY = 0

    TURNS = (
        BLACK,
        WHITE,
    )

    State = namedtuple('State', ['board', 'turn', 'score'])

    def __init__(self, boardArray):
        self.boardArray = boardArray

        print("TURNS: ", self.TURNS[0], self.TURNS[1])

        # Turn counter
        self._turn = self.BLACK

        # Player scores
        self._score = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Game history
        self._history = []
        self._redo = []

    @property
    def _next_turn(self):
        """
        Gets color of next turn.
        """
        return self.TURNS[self._turn is self.BLACK]

    def move(self, x, y):
        """
        Makes a move at the given location for the current turn's color.
        """
        # Check if coordinates are occupied
        if self.boardArray[x-1][y-1] is not self.EMPTY:
            print('Cannot move on top of another piece!')
            return

        print("self.boardArray[x][y]: ", self.boardArray[x-1][y-1], ",x: ", x, ", y:", y)

        # Store history and make move
        # self._push_history()
        self.boardArray[x-1][y-1] = self._turn

        # Check if any pieces have been taken
        #taken = self._take_pieces(x-1, y-1)

        # Check if move is suicidal.  A suicidal move is a move that takes no
        # pieces and is played on a coordinate which has no liberties.
        #if taken == 0:
        #    self._check_for_suicide(x-1, y-1)

        # Check if move is redundant.  A redundant move is one that would
        # return the board to the state at the time of a player's last move.
        #self._check_for_ko()

        self._flip_turn()
        self._redo = []

    def _flip_turn(self):
        """
        Iterates the turn counter.
        """
        self._turn = self._next_turn
        return self._turn

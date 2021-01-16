from copy import copy, deepcopy


class GameLogic:
    print("Game Logic Object Created")

    FREE = 0
    BLACK = 1
    WHITE = 2

    PLAYERS = (
        BLACK,
        WHITE,
    )

    def __init__(self, board_width):
        self.board_array = [[0 for _ in range(board_width)] for _ in range(board_width)]

        # The blacks starts first by the rules
        self.current_player = self.BLACK

        # self.previous_players is used to check if a player passes more than once in a row
        self.previous_players = 4 * [self.FREE]

        # game is not currently started
        self.is_started = False

        # pass_counts used to track if a player passes more than once in a row
        # and the next player player his/her turn
        self.pass_counts = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # pass_counts_without_move used to track if a player passes more than once in a row
        # without any move from either player
        self.pass_counts_without_move = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Points of each player
        self.point = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Stores the historical data of the current game
        self.game_data = []

    def tryMove(self, x, y):
        """
        Move to the given coordinates for the current player.
        Returns:
            0 - if it was successful
            1 - if the coordinate is not free
            2 - if the move is a suicide move
            3 - if the move is a KO move
        """
        # Game has started
        self.is_started = True
        # Check if coordinates are occupied
        if self.board_array[x][y] is not self.FREE:
            print('The coordinate is not free!')
            return 1

        # Store state
        self.saveData()
        self.board_array[x][y] = self.current_player

        # Check if any stones have been captured
        captured = self.captureStones(x, y)

        # Check for suicidal tryMove
        if captured == 0:
            if self.isSuicidal(x, y):
                # Set the coordinates back to free as we are not making a move
                self.board_array[x][y] = self.FREE
                print('It is a suicidal move!')
                return 2

        # Check for KO tryMove
        if self.isKo():
            # Set the coordinates back to free as we are not making a move
            self.board_array[x][y] = self.FREE
            print('It is a KO move!')
            return 3

        # reset pass_counts_without_move
        self.pass_counts_without_move = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Move on to the next player
        self.changePlayerTurn()
        # Return 0 as we succeeded all the previous steps
        return 0

    def changePlayerTurn(self):
        """
        Changes the turn to the next player
        """
        print("self.pass_counts: ", self.pass_counts,
              ", self.previous_players: ", self.previous_players,
              ", self.current_player: ", self.current_player)
        if self.current_player not in self.previous_players:
            print("Reset pass counts")
            self.pass_counts[self.current_player] = 0

        self.previous_players[0] = self.previous_players[1]
        self.previous_players[1] = self.previous_players[2]
        self.previous_players[2] = self.previous_players[3]
        self.previous_players[3] = self.current_player

        self.current_player = self.nextPlayer

    def passTurn(self):
        """pass current player's turn, returns True if the current player loose"""
        self.pass_counts[self.current_player] += 1
        self.pass_counts_without_move[self.current_player] += 1

        print("passTurn: self.pass_counts: ", self.pass_counts,
              ", self.pass_counts_without_move: ", self.pass_counts_without_move,
              ", self.previous_players: ", self.previous_players,
              ", self.current_player: ", self.current_player)

        if self.pass_counts[self.current_player] == 2 or self.pass_counts_without_move[self.current_player] == 2:
            print("Player: {} lost the game after two passes in a row".format(self.currentPlayerColour))
            return True

        self.current_player = self.nextPlayer
        return False

    def isSuicidal(self, x, y):
        """Checks if tryMove is suicidal"""
        if self.numLiberties(x, y) == 0:
            self.readData()
            print('Cannot play on a coordinate with no liberties!')
            return True

        return False

    def isKo(self):
        """Checks if the state is KO, which means it is redundant"""
        try:
            if self.board_array == self.game_data[-2][0]:
                self.readData()
                print('Cannot make a tryMove that is redundant!')
                return True
        except IndexError as e:
            print("IndexError in isKo: {}".format(str(e)))
            return False

        return False

    def captureStones(self, x, y):
        """
        If any stones was taken by the last tryMove at the given
        coordinates then removes it from the game and adds it up the points.
        """
        points = []
        # get all surrounding coordinates to a location
        for c, (x1, y1) in self.getSurroundingCoords(x, y):
            # if the surrounding is the next player with no liberties then take it
            if c is self.nextPlayer and self.numLiberties(x1, y1) == 0:
                point = self.captureStoneGroup(x1, y1)
                # add the point into the list to sum it up later
                points.append(point)
                self.addPoint(point)
        return sum(points)

    def loadGameState(self, state):
        """
        Loads the specified game state
        """
        if len(state) != 3:
            print("ERROR: game is in unstable state")
            return

        self.board_array = state[0]
        self.current_player = state[1]
        print("game_data: ", self.game_data)
        print("self.point: ", self.point, ", state[2]: ", state[2])
        self.point = state[2]

    def saveData(self):
        """
        Saves game state.
        """
        self.game_data.append(self.state)

    def readData(self):
        """
        Reads game data from saved state.
        """
        current_state = self.state
        try:
            self.loadGameState(self.game_data.pop())
            return current_state
        except IndexError as e:
            print("IndexError in readData: {}".format(str(e)))
            return None

    def addPoint(self, point):
        """
        Adds point to the current player's total points.
        """
        self.point[self.current_player] += point
        print("self.point: ", self.point)

    def xyValue(self, x, y):
        """
        Returns value of (x, y) of board_array if it exists, None otherwise.
        """
        try:
            return self.board_array[x][y]
        except IndexError as e:
            print("IndexError in xyValue: {}".format(str(e)))
            return None

    def getSurroundingCoords(self, x, y):
        """
        Returns a tuple of the clockwise surrounding coordinates of the given coordinate
        """
        # Four surrounding coordinates: north, south, west, east
        # it does not include a free coordinate.
        coordinates = ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y))
        return [(self.xyValue(x, y), (x, y)) for x, y in coordinates if self.xyValue(x, y) is not None]

    def getColourGroup(self, x, y, visited):
        """
        Traverses adjacent coordinates of the same color and finds all
        group member coordinates.
        """
        colour = self.board_array[x][y]
        # non-visited surrounding coordinates with the same color
        surrounding_coords = [
            (c, (i, j)) for c, (i, j) in self.getSurroundingCoords(x, y)
            if c is colour and (i, j) not in visited
        ]

        # Mark the current coordinates as visited
        visited.add((x, y))

        # coordinates with the same colour
        if surrounding_coords:
            colour_group_coords = [self.getColourGroup(i, j, visited) for _, (i, j) in surrounding_coords]
            return visited.union(*colour_group_coords)

        return visited

    def getStoneGroup(self, x, y):
        """
        Gets all coordinates for the members of the same
        group at the given coordinates.
        """
        if self.board_array[x][y] not in self.PLAYERS:
            print('Error: Unknown game state')
            return

        return self.getColourGroup(x, y, set())

    def captureStoneGroup(self, x, y):
        """
        Captures multiple stones, i.e. a group of black or white stones and returns the group size.
        """
        if self.board_array[x][y] not in self.PLAYERS:
            print('Cannot capture unknown player')
            return

        stone_group = self.getStoneGroup(x, y)
        point = len(stone_group)

        for x1, y1 in stone_group:
            self.board_array[x1][y1] = self.FREE

        return point

    def getLibertiesSet(self, x, y, visited):
        """
        Recursively traverses adjacent surrounding_coords of the same color to find all
        surrounding liberties for the group at the given coordinates.
        """
        colour = self.board_array[x][y]

        if colour is self.FREE:
            return set([(x, y)])

        # We need to get the surrounding surrounding_coords which are free or have the same color
        # with no visited coordinates
        surrounding_coords = [
            (c, (i, j))
            for c, (i, j) in self.getSurroundingCoords(x, y)
            if (c is colour or c is self.FREE) and (i, j) not in visited
        ]

        # print("surrounding_coords: ", surrounding_coords, ", visited: ", visited, ", colour: ", colour)
        # print("l.self.getSurroundingCoords({}, {}): {}".format(x, y, self.getSurroundingCoords(x, y)))

        # Mark current coordinates as having been visited to avoid double processing/loop
        visited.add((x, y))

        # We need to collect unique coordinates of all surrounding liberties
        if surrounding_coords:
            liberties_coords = [
                self.getLibertiesSet(i, j, visited)
                for _, (i, j) in surrounding_coords
            ]
            return set.union(*liberties_coords)

        # if surrounding_coords was empty we reach here and return an empty set
        return set()

    def getLiberties(self, x, y):
        """
        Collects the coordinates for liberties surrounding the group at the given
        coordinates.
        """
        return self.getLibertiesSet(x, y, set())

    def numLiberties(self, x, y):
        """
        Gets the number of liberties surrounding the group at the given
        coordinates.
        """
        return len(self.getLiberties(x, y))

    # Class properties below
    @property
    def nextPlayer(self):
        """
        Calculate the index/colour of the next player.
        """
        # PLAYERS[0] = BLACK, PLAYERS[1] = WHITE, therefore if the current
        # player is black, the next one is white, if the current player is white
        # the next one is black.
        index = self.current_player is self.BLACK
        return self.PLAYERS[index]

    @property
    def currentPlayerColour(self):
        """it returns the current player colour"""
        colour = "None"
        if self.current_player is self.BLACK:
            colour = "Black"
        elif self.current_player is self.WHITE:
            colour = "White"

        return colour


    @property
    def playerPoints(self):
        """
        Returns the player points as a json object.
        """
        return self.point[self.BLACK], self.point[self.WHITE]

    @property
    def state(self):
        """
        Returns the game state (board, current player, and points) as a tuple.
        """
        return deepcopy(self.board_array[:]), self.current_player, copy(self.point)

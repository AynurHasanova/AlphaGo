from copy import copy


class GameLogic:
    print("Game Logic Object Created")

    FREE = 0
    BLACK = 1
    WHITE = 2

    PLAYERS = (
        BLACK,
        WHITE,
    )

    def __init__(self, board_array):
        self.board_array = board_array

        # The blacks starts first by the rules
        self.current_player = self.BLACK

        # game is not currently started
        self.is_started = False

        # whether the pass button clicked
        self.passed = False

        # Points of each player
        self.point = {
            self.BLACK: 0,
            self.WHITE: 0,
        }

        # Stores the historical data of the current game
        self.game_data = []

    def try_move(self, x, y):
        """
        Move to the given coordinates for the current player. Returns true if successful
        """
        # Game has started
        self.is_started = True
        # Check if coordinates are occupied
        if self.board_array[x][y] is not self.FREE:
            print('The coordinate is not free!')
            return False

        # Store state
        self.save_data()
        self.board_array[x][y] = self.current_player

        # Check if any stones have been captured
        captured = self.capture_stones(x, y)

        # Check for suicidal tryMove
        if captured == 0:
            if self.is_suicidal(x, y):
                # Set the coordinates back to free as we are not making a move
                self.board_array[x][y] = self.FREE
                return False

        # Check for KO tryMove
        #if self.isKo():
            # Set the coordinates back to free as we are not making a move
        #    self.board_array[x][y] = self.FREE
        #    return False

        # Move on to the next player
        self.change_player_turn(False)
        # Return true as we succeeded all the previous steps
        return True

    def change_player_turn(self, passed):
        """
        Changes the turn to the next player.
        """
        self.current_player = self.next_player
        self.passed = passed
        return self.current_player

    def is_suicidal(self, x, y):
        """
        Checks if tryMove is suicidal
        """
        if self.num_liberties(x, y) == 0:
            self.read_data()
            print('Cannot play on a coordinate with no liberties!')
            return True

        return False

    def is_ko(self):
        """
        Checks if the state is KO, which means it is redundant.
        """
        try:
            print("self.game_data[-2][0]", self.game_data[-2][0])
            if self.board_array == self.game_data[-2][0]:
                self.read_data()
                print('Cannot make a tryMove that is redundant!')
                return True
        except IndexError as e:
            print("IndexError in isKo: {}".format(str(e)))
            return False

        return False

    def capture_stones(self, x, y):
        """
        If any stones was taken by the last tryMove at the given
        coordinates then removes it from the game and adds it up the pointsAndTerritories.
        """
        points = []
        for c, (x1, y1) in self.get_surrounding_coords(x, y):
            if c is self.next_player and self.num_liberties(x1, y1) == 0:
                point = self.capture_stone_group(x1, y1)
                print("Captured pointsAndTerritories: ", point)
                points.append(point)
                self.add_point(point)
        return sum(points)

    def load_game_state(self, state):
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

    def save_data(self):
        """
        Saves game state.
        """
        self.game_data.append(self.state)

    def read_data(self):
        """
        Reads game data from saved state.
        """
        current_state = self.state
        try:
            self.load_game_state(self.game_data.pop())
            return current_state
        except IndexError as e:
            print("IndexError in readData: {}".format(str(e)))
            return None

    def add_point(self, point):
        """
        Adds point to the current player's total pointsAndTerritories.
        """
        self.point[self.current_player] += point
        print("self.point: ", self.point)

    def xy_value(self, x, y):
        """
        Returns value of (x, y) of board_array if it exists, None otherwise.
        """
        try:
            return self.board_array[x][y]
        except IndexError as e:
            print("IndexError in xyValue: {}".format(str(e)))
            return None

    def get_surrounding_coords(self, x, y):
        """
        Returns a tuple of the clockwise surrounding coordinates of the given coordinate
        """
        # Four surrounding coordinates: north, south, west, east
        # it does not include a free coordinate.
        coordinates = ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y))
        return [(self.xy_value(x, y), (x, y)) for x, y in coordinates if self.xy_value(x, y) is not None]

    def get_colour_group(self, x, y, visited):
        """
        Traverses adjacent coordinates of the same color and finds all
        group member coordinates.
        """
        colour = self.board_array[x][y]
        # non-visited surrounding coordinates with the same color
        surrounding_coords = [
            (c, (i, j)) for c, (i, j) in self.get_surrounding_coords(x, y)
            if c is colour and (i, j) not in visited
        ]

        # Mark the current coordinates as visited
        visited.add((x, y))

        # coordinates with the same colour
        if surrounding_coords:
            colour_group_coords = [self.get_colour_group(i, j, visited) for _, (i, j) in surrounding_coords]
            return visited.union(*colour_group_coords)

        return visited

    def get_stone_group(self, x, y):
        """
        Gets all coordinates for the members of the same
        group at the given coordinates.
        """
        if self.board_array[x][y] not in self.PLAYERS:
            print('Error: Unknown game state')
            return

        return self.get_colour_group(x, y, set())

    def capture_stone_group(self, x, y):
        """
        Captures multiple stones, i.e. a group of black or white stones and returns the group size.
        """
        if self.board_array[x][y] not in self.PLAYERS:
            print('Cannot capture unknown player')
            return

        stone_group = self.get_stone_group(x, y)
        point = len(stone_group)

        for x1, y1 in stone_group:
            self.board_array[x1][y1] = self.FREE

        return point

    def get_liberties_set(self, x, y, visited):
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
            for c, (i, j) in self.get_surrounding_coords(x, y)
            if (c is colour or c is self.FREE) and (i, j) not in visited
        ]

        # print("surrounding_coords: ", surrounding_coords, ", visited: ", visited, ", colour: ", colour)
        # print("l.self.getSurroundingCoords({}, {}): {}".format(x, y, self.getSurroundingCoords(x, y)))

        # Mark current coordinates as having been visited to avoid double processing/loop
        visited.add((x, y))

        # We need to collect unique coordinates of all surrounding liberties
        if surrounding_coords:
            liberties_coords = [
                self.get_liberties_set(i, j, visited)
                for _, (i, j) in surrounding_coords
            ]
            return set.union(*liberties_coords)

        # if surrounding_coords was empty we reach here and return an empty set
        return set()

    def get_liberties(self, x, y):
        """
        Collects the coordinates for liberties surrounding the group at the given
        coordinates.
        """
        return self.get_liberties_set(x, y, set())

    def num_liberties(self, x, y):
        """
        Gets the number of liberties surrounding the group at the given
        coordinates.
        """
        return len(self.get_liberties(x, y))

    # Class properties below
    @property
    def next_player(self):
        """
        Calculate the index/colour of the next player.
        """
        # PLAYERS[0] = BLACK, PLAYERS[1] = WHITE, therefore if the current
        # player is black, the next one is white, if the current player is white
        # the next one is black.
        index = self.current_player is self.BLACK
        return self.PLAYERS[index]

    @property
    def next_player_colour(self):
        if self.is_started and (not self.passed):
            if self.current_player is self.BLACK:
                return "WHITE"
            elif self.current_player is self.WHITE:
                return "BLACK"
            else:
                return "NONE"
        else:
            # Reset passed flag
            self.passed = False
            if self.current_player is self.BLACK:
                return "BLACK"
            elif self.current_player is self.WHITE:
                return "WHITE"
            else:
                return "NONE"

    @property
    def player_points(self):
        """
        Returns the player pointsAndTerritories as a json object.
        """
        return "(B:{}, W:{})".format(self.point[self.BLACK], self.point[self.WHITE])

    @property
    def state(self):
        """
        Returns the game state (board, current player, and pointsAndTerritories) as a tuple.
        """
        return self.board_array[:], self.current_player, copy(self.point)

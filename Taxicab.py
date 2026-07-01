class Taxicab:
    """
    Represents a taxicab with x-coordinate, y-coordinate, and odometer.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes the taxicab with x and y coordinates.
        The odometer starts at zero.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the current x-coordinate.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the current y-coordinate.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the current odometer reading.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the taxicab left or right and updates the odometer.
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the taxicab up or down and updates the odometer.
        """
        self._y_coord += distance
        self._odometer += abs(distance)

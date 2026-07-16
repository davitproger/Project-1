# Author: Davil Gabdulinov
# GitHub username: davitproger
# Date: July 15, 2026
# Description: Defines a Box class and sorts a list of Box objects from
# greatest volume to least volume using insertion sort.


class Box:
    """Represents a box with a length, width, and height."""

    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def volume(self):
        """Return the volume of the box."""
        return self.__length * self.__width * self.__height


def box_sort(box_list):
    """Sort a list of boxes from greatest volume to least volume."""
    for current_index in range(1, len(box_list)):
        current_box = box_list[current_index]
        current_volume = current_box.volume()

        previous_index = current_index - 1

        # Shift smaller boxes one position to the right.
        while previous_index >= 0 and box_list[previous_index].volume() < current_volume:
            box_list[previous_index + 1] = box_list[previous_index]
            previous_index -= 1

        # Insert the current box into its correct position.
        box_list[previous_index + 1] = current_box
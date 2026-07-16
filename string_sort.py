# Author: Davil Gabduldinov
# GitHub username: davitproger
# Date: July 15, 2026
# Description: Sorts a list of strings in alphabetical order using
# insertion sort while ignoring letter case.


def string_sort(string_list):
    """Sort a list of strings alphabetically, ignoring case."""
    for current_index in range(1, len(string_list)):
        current_string = string_list[current_index]

        previous_index = current_index - 1

        # Shift larger strings one position to the right.
        while previous_index >= 0 and string_list[previous_index].lower() > current_string.lower():
            string_list[previous_index + 1] = string_list[previous_index]
            previous_index -= 1

        # Insert the current string into its correct position.
        string_list[previous_index + 1] = current_string
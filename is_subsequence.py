# Author: Davil Gabduldinov
# GitHub username: davitproger
# Date: 07/20/2026
# Description: Recursively determines whether the first string is a
# subsequence of the second string.


def is_subsequence(first_string, second_string):
    """Return True if the first string is a subsequence of the second."""
    if first_string == "":
        return True

    if second_string == "":
        return False

    if first_string[0] == second_string[0]:
        return is_subsequence(first_string[1:], second_string[1:])

    return is_subsequence(first_string, second_string[1:])
# Author: Davil Gabduldinov
# GitHub username: davitproger
# Date: 07/20/2026
# Description: Determines whether the numbers in a list are strictly
# decreasing by using recursion.


def is_decreasing(numbers):
    """Return True if the numbers in the list are strictly decreasing."""
    if len(numbers) == 1:
        return True

    if numbers[0] <= numbers[1]:
        return False

    return is_decreasing(numbers[1:])
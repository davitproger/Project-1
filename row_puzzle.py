# Author: Davil Gabduldinov
# GitHub username: davitproger
# Date: 07/20/2026
# Description: Recursively determines whether a row puzzle can be solved.


def row_puzzle(row):
    """Return True if the row puzzle can be solved, otherwise False."""
    return _solve(row, 0, set())


def _solve(row, index, visited):
    """Recursively explore all possible moves from the current index."""

    if index < 0 or index >= len(row):
        return False

    if index == len(row) - 1:
        return True

    if index in visited:
        return False

    visited.add(index)

    jump = row[index]

    return (_solve(row, index + jump, visited) or
            _solve(row, index - jump, visited))
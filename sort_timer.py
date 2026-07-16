# Author: Davil Gabduldinov
# GitHub username: davitproger
# Date: July 15, 2026
# Description: Compares the running times of bubble sort and insertion
# sort on randomly generated lists and displays the results on a graph.

import random
import time
from matplotlib import pyplot


def bubble_time(number_list):
    """Sort a list using bubble sort and return the elapsed time."""
    start_time = time.perf_counter()

    for pass_number in range(len(number_list) - 1):
        for current_index in range(len(number_list) - 1 - pass_number):
            next_index = current_index + 1

            if number_list[current_index] > number_list[next_index]:
                temporary_value = number_list[current_index]
                number_list[current_index] = number_list[next_index]
                number_list[next_index] = temporary_value

    end_time = time.perf_counter()
    return end_time - start_time


def insertion_time(number_list):
    """Sort a list using insertion sort and return the elapsed time."""
    start_time = time.perf_counter()

    for current_index in range(1, len(number_list)):
        current_value = number_list[current_index]
        previous_index = current_index - 1

        while previous_index >= 0 and number_list[previous_index] > current_value:
            number_list[previous_index + 1] = number_list[previous_index]
            previous_index -= 1

        number_list[previous_index + 1] = current_value

    end_time = time.perf_counter()
    return end_time - start_time


def sort_times_for_random_list(list_length):
    """Return bubble sort and insertion sort times for a random list."""
    first_list = []

    for unused_number in range(list_length):
        random_number = random.randint(1, list_length)
        first_list.append(random_number)

    second_list = list(first_list)

    bubble_sort_time = bubble_time(first_list)
    insertion_sort_time = insertion_time(second_list)

    return bubble_sort_time, insertion_sort_time


def compare_sorts():
    """Display a graph comparing bubble sort and insertion sort times."""
    list_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    bubble_times = []
    insertion_times = []

    for list_length in list_lengths:
        bubble_sort_time, insertion_sort_time = sort_times_for_random_list(list_length)
        bubble_times.append(bubble_sort_time)
        insertion_times.append(insertion_sort_time)

    pyplot.plot(list_lengths, bubble_times, "ro--", linewidth=2, label="Bubble Sort")
    pyplot.plot(list_lengths, insertion_times, "go--", linewidth=2, label="Insertion Sort")
    pyplot.xlabel("Size of List Being Sorted")
    pyplot.ylabel("Seconds to Sort")
    pyplot.legend(loc="upper left")
    pyplot.show()


def main():
    """Run the sorting comparison and display the graph."""
    compare_sorts()


if __name__ == "__main__":
    main()
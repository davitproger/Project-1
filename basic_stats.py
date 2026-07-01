import statistics

class Student:
    """
    Represents a student with a name and a grade.
    """

    def __init__(self, name, grade):
        """
        Initializes the student's name and grade.
        """
        self._name = name
        self._grade = grade

    def get_grade(self):
        """
        Returns the student's grade.
        """
        return self._grade

def basic_stats(student_list):
    """
    Returns the mean, median, and mode of the student grades.
    """
    grades = []

    for student in student_list:
        grades.append(student.get_grade())

    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)

    return (mean, median, mode)

"""Assignment 2 - a single class: Student."""


class Student:
    """A university student with four attributes and two constructors."""

    def __init__(self, name=None, student_id=None, major=None, gpa=None):
        """Parameterized constructor.

        Called with no arguments it acts as the 'default' constructor:
        every field becomes None.
        """
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    @classmethod
    def default(cls):
        """Explicit default constructor: all fields None."""
        return cls()

    def display_info(self):
        """Print the student's details in a readable form."""
        print("-" * 30)
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Major      : {self.major}")
        print(f"GPA        : {self.gpa}")
        print(f"Standing   : {self.academic_standing()}")

    def academic_standing(self):
        """Second meaningful method: classify by GPA."""
        if self.gpa is None:
            return "Unknown"
        if self.gpa >= 3.5:
            return "Honours"
        if self.gpa >= 2.0:
            return "Good standing"
        return "Probation"

    def __str__(self):
        return f"Student({self.name}, ID={self.student_id}, {self.major}, GPA={self.gpa})"

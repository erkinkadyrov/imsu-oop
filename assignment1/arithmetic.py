"""Assignment 1 - Basic Programming & Precision Arithmetic (tasks 1-5)."""
import math


def rectangle_perimeter_area(a, b):
    """Task 1: perimeter and area of a rectangle with sides a, b."""
    return 2 * (a + b), a * b


def hypotenuse(a, b):
    """Task 2: hypotenuse of a right triangle by legs a, b."""
    return math.sqrt(a * a + b * b)


def digit_sum_3(n):
    """Task 3: sum of digits of a three-digit number."""
    n = abs(n)
    return n // 100 + (n // 10) % 10 + n % 10


def time_to_seconds(h, m, s):
    """Task 4: convert (hours, minutes, seconds) to total seconds."""
    return h * 3600 + m * 60 + s


def minutes_to_dhm(total):
    """Task 5: convert total minutes to (days, hours, minutes)."""
    days = total // (24 * 60)
    rest = total % (24 * 60)
    hours = rest // 60
    minutes = rest % 60
    return days, hours, minutes


if __name__ == "__main__":
    a, b = int(input("a = ")), int(input("b = "))
    p, s = rectangle_perimeter_area(a, b)
    print(f"Perimeter = {p}, Area = {s}")

    c1, c2 = int(input("leg a = ")), int(input("leg b = "))
    print(f"Hypotenuse = {hypotenuse(c1, c2)}")

    print(f"Digit sum = {digit_sum_3(int(input('3-digit number = ')))}")

    h, m, s = int(input("h = ")), int(input("m = ")), int(input("s = "))
    print(f"Total seconds = {time_to_seconds(h, m, s)}")

    d, hh, mm = minutes_to_dhm(int(input("total minutes = ")))
    print(f"{d} days, {hh} hours, {mm} minutes")

"""Assignment 1 - Conditions (tasks 6-10)."""


def maximum(a, b):
    """Task 6: maximum of two numbers."""
    return a if a > b else b


def even_odd(n):
    """Task 7: even / odd."""
    return "Even" if n % 2 == 0 else "Odd"


def valid_time(h, m):
    """Task 8: is hh:mm a valid 24-hour time."""
    return "Valid" if 0 <= h <= 23 and 0 <= m <= 59 else "Invalid"


def quadrant(x, y):
    """Task 9: quadrant or axis for point (x, y)."""
    if x == 0 and y == 0:
        return "Origin"
    if x == 0:
        return "On Y axis"
    if y == 0:
        return "On X axis"
    if x > 0 and y > 0:
        return "Quadrant 1"
    if x < 0 and y > 0:
        return "Quadrant 2"
    if x < 0 and y < 0:
        return "Quadrant 3"
    return "Quadrant 4"


def segments_overlap(a, b, c, d):
    """Task 10: do segments [a, b] and [c, d] overlap."""
    lo1, hi1 = min(a, b), max(a, b)
    lo2, hi2 = min(c, d), max(c, d)
    return "Overlapping" if max(lo1, lo2) <= min(hi1, hi2) else "Not overlapping"


if __name__ == "__main__":
    a, b = int(input("a = ")), int(input("b = "))
    print("Max =", maximum(a, b))

    print(even_odd(int(input("n = "))))

    h, m = int(input("hour = ")), int(input("minute = "))
    print(valid_time(h, m))

    x, y = int(input("x = ")), int(input("y = "))
    print(quadrant(x, y))

    a, b = int(input("segment1 a = ")), int(input("segment1 b = "))
    c, d = int(input("segment2 c = ")), int(input("segment2 d = "))
    print(segments_overlap(a, b, c, d))

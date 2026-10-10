"""Assignment 1 - While Loop (tasks 16-20)."""


def digit_sum_while(n):
    """Task 16: sum of digits using while."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def gcd(a, b):
    """Task 17: greatest common divisor (Euclid)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def to_binary(n):
    """Task 18: decimal to binary string."""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits


def read_in_range_1_10():
    """Task 19: do-while - keep asking for a number in 1..10."""
    while True:
        value = int(input("Enter a number 1..10: "))
        if 1 <= value <= 10:
            return value


def sum_until_zero():
    """Task 20: read numbers until 0, return the sum."""
    total = 0
    while True:
        value = int(input("Number (0 to stop): "))
        if value == 0:
            break
        total += value
    return total


if __name__ == "__main__":
    print("Digit sum:", digit_sum_while(int(input("n = "))))
    a, b = int(input("a = ")), int(input("b = "))
    print("GCD:", gcd(a, b))
    print("Binary:", to_binary(int(input("decimal = "))))
    print("Accepted:", read_in_range_1_10())
    print("Sum:", sum_until_zero())

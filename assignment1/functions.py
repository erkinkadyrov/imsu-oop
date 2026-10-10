"""Assignment 1 - Functions (tasks 21-25)."""


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def count_primes(a, b):
    """Task 21: how many primes in range [a, b]."""
    return sum(1 for n in range(a, b + 1) if is_prime(n))


def decimal_to_binary(n):
    """Task 22: decimal to binary string via a loop."""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits


def hollow_square(n):
    """Task 23: hollow N x N square of stars."""
    lines = []
    for i in range(n):
        if i == 0 or i == n - 1:
            lines.append("*" * n)
        else:
            lines.append("*" + " " * (n - 2) + "*")
    return "\n".join(lines)


def inverted_pyramid(n):
    """Task 24: inverted isosceles pyramid of height n."""
    lines = []
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        lines.append(spaces + stars)
    return "\n".join(lines)


def armstrong_numbers():
    """Task 25: all Armstrong numbers 100..999."""
    result = []
    for n in range(100, 1000):
        a, b, c = n // 100, (n // 10) % 10, n % 10
        if a ** 3 + b ** 3 + c ** 3 == n:
            result.append(n)
    return result


if __name__ == "__main__":
    a, b = int(input("A = ")), int(input("B = "))
    print("Primes in range:", count_primes(a, b))
    print("Binary:", decimal_to_binary(int(input("decimal = "))))
    n = int(input("N for square = "))
    print(hollow_square(n))
    print(inverted_pyramid(int(input("N for pyramid = "))))
    print("Armstrong 100..999:", *armstrong_numbers())

"""Assignment 1 - For Loop (tasks 11-15)."""


def multiples_of_3_and_5(n):
    """Task 11: numbers 1..n divisible by both 3 and 5."""
    return [i for i in range(1, n + 1) if i % 3 == 0 and i % 5 == 0]


def factorial(n):
    """Task 12: factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def number_triangle(n):
    """Task 13: right triangle of numbers, height n (nested loops)."""
    lines = []
    for i in range(1, n + 1):
        lines.append(" ".join(str(j) for j in range(1, i + 1)))
    return "\n".join(lines)


def sum_of_squares(n):
    """Task 14: sum of squares 1..n."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def multiplication_tables(n):
    """Task 15: multiplication tables 1..n (nested loops)."""
    blocks = []
    for i in range(1, n + 1):
        rows = [f"{i} x {j} = {i * j}" for j in range(1, n + 1)]
        blocks.append("\n".join(rows))
    return "\n\n".join(blocks)


if __name__ == "__main__":
    n = int(input("N = "))
    print("Multiples of 3 and 5:", *multiples_of_3_and_5(n))
    print("Factorial:", factorial(n))
    print("Triangle:")
    print(number_triangle(n))
    print("Sum of squares:", sum_of_squares(n))
    print("Multiplication tables:")
    print(multiplication_tables(n))

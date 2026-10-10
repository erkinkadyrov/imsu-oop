"""Assignment 1 - Basic Array Operations & Sequences (tasks 26-35)."""
import random


def divide_by_max(arr):
    """Task 26: divide every element by the maximum."""
    m = max(arr)
    return [x / m for x in arr]


def first_positive(arr):
    """Task 27: index and value of the first positive element."""
    for i, x in enumerate(arr):
        if x > 0:
            return i, x
    return -1, None


def negate_all(arr):
    """Task 28: replace every element with its opposite sign."""
    return [-x for x in arr]


def swap_min_max(arr):
    """Task 29: find min and max and swap them."""
    arr = arr[:]
    i_min, i_max = arr.index(min(arr)), arr.index(max(arr))
    arr[i_min], arr[i_max] = arr[i_max], arr[i_min]
    return arr


def max_minus_min(arr):
    """Task 30: difference between max and min."""
    return max(arr) - min(arr)


def count_local_maxima(arr):
    """Task 31: count elements strictly greater than both neighbours."""
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count


def replace_less_than_15(arr):
    """Task 32: replace every value < 15 with -1."""
    return [-1 if x < 15 else x for x in arr]


def random_array(n, a, b):
    """Task 33: fill an array with n random numbers in [a, b]."""
    return [random.randint(a, b) for _ in range(n)]


def sum_of_min_max_indices(arr):
    """Task 34: sum of indices of the min and max elements."""
    return arr.index(min(arr)) + arr.index(max(arr))


def sum_between_zeros(arr):
    """Task 35: sum of elements between the first and last zero."""
    if 0 not in arr:
        return 0
    first = arr.index(0)
    last = len(arr) - 1 - arr[::-1].index(0)
    return sum(arr[first + 1:last])


if __name__ == "__main__":
    data = [5, 3, 11, 2, 7]
    print("Source:", data)
    print("Divide by max:", divide_by_max(data))
    print("First positive (index, value):", first_positive([-3, -1, 0, 2, 9]))
    print("Negate all:", negate_all(data))
    print("Swap min/max:", swap_min_max(data))
    print("Max - min:", max_minus_min(data))
    print("Local maxima:", count_local_maxima([1, 3, 1, 5, 2, 6, 4]))
    print("Replace <15:", replace_less_than_15([10, 20, 5, 40]))
    print("Random array:", random_array(5, 1, 100))
    print("Sum of min/max indices:", sum_of_min_max_indices(data))
    print("Sum between zeros:", sum_between_zeros([1, 0, 4, 5, 6, 0, 9]))

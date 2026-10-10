"""Assignment 1 - Strings (tasks 36-40)."""

VOWELS = "aeiou"


def is_palindrome(s):
    """Task 36: palindrome check."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return "Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome"


def to_upper(s):
    """Task 37: convert a string to upper case."""
    return s.upper()


def count_consonants(s):
    """Task 38: count consonants."""
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in VOWELS)


def count_vowels(s):
    """Task 39: count vowels."""
    return sum(1 for ch in s.lower() if ch in VOWELS)


def count_words(s):
    """Task 40: count words."""
    return len(s.split())


if __name__ == "__main__":
    print(is_palindrome(input("Word: ")))
    print(to_upper(input("String: ")))
    text = input("Text: ")
    print("Consonants:", count_consonants(text))
    print("Vowels:", count_vowels(text))
    print("Words:", count_words(text))

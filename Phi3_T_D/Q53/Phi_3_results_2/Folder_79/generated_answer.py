from itertools import product

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindrome_of_length_at_least_n(string):
    unique_chars = ''.join(set((char.lower() for char in string if char.isalpha())))
    palindromes = set()
    for length in range(17, len(string) + 1):
        for start in range(0, len(string) - length + 1):
            substring = ''.join(sorted(string[start:start + length].lower()))
            if is_palindrome(substring) and all((char in unique_chars for char in substring)):
                palindromes.add(substring.lower())
    return palindromes
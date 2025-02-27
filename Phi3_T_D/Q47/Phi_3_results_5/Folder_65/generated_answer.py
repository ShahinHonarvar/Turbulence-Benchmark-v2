from itertools import product

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def palindromes_of_specific_lengths(text):
    prefix = text[15:96]
    palindromes = set()
    for length in range(20, 67):
        for start in range(len(prefix) - length + 1):
            substring = prefix[start:start + length]
            if substring.isalpha() and ' ' not in substring and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
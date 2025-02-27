import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    for i in range(12, 93 - 42 + 2):
        for len_ in range(42, 78):
            substr = s[i:i + len_]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes
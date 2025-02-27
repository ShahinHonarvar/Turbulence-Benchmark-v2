import re

def palindromes_of_specific_lengths(s):
    substring = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                palindromes.add(potential_palindrome.lower())
    return palindromes
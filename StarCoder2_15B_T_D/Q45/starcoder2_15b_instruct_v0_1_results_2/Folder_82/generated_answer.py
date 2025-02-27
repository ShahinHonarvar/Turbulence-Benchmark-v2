import re

def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(1, len(string) - 6):
        for j in range(i + 6, len(string)):
            substring = string[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes

def is_palindrome(string):
    return string == string[::-1]
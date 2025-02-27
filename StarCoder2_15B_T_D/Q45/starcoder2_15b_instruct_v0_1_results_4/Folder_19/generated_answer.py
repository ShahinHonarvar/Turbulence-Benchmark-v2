import re

def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for permutation in permutations(letters, len(letters)):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 7 and is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes

def is_palindrome(string):
    return string.lower() == string[::-1].lower()
import re

def palindromes_between_indices(string):
    letters = set(re.findall('[a-zA-Z]', string))
    palindromes = set()
    for combination in combinations(letters, 5):
        if is_palindrome(''.join(combination)):
            palindromes.add(''.join(combination))
    return palindromes

def is_palindrome(string):
    return string.lower() == string.lower()[::-1]
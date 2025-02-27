from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[1:9]
    substring_letters = [char.lower() for char in substring if char.isalpha()]
    unique_letters = ''
    for letter in substring_letters:
        if letter not in unique_letters:
            unique_letters += letter
    candidate_palindromes = set((''.join(p) for p in permutations(unique_letters, 6)))
    result = {palindrome for palindrome in candidate_palindromes if is_palindrome(palindrome)}
    return result
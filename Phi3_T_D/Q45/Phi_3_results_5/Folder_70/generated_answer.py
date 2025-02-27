from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    letters_range = text[1:7]
    unique_letters = set(letters_range.lower()) - {' '}
    palindromes = {''.join(p) for p in permutations(unique_letters) if len(p) >= 4 and is_palindrome(''.join(p))}
    return palindromes
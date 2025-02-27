from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    substring = s[0:5].lower()
    letters = set(substring)
    possible_words = set((''.join(p) for p in permutations(letters, len(letters))))
    return {word for word in possible_words if is_palindrome(word) and len(word) >= 3}
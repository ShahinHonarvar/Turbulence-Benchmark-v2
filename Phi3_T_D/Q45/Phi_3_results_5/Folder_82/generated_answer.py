from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:7]]
    letter_set = set(letters)
    if len(letter_set) < 7:
        return set()
    palindrome_set = set()
    for perm in permutations(letter_set, 7):
        joined = ''.join(perm)
        if is_palindrome(joined):
            palindrome_set.add(joined)
    return palindrome_set
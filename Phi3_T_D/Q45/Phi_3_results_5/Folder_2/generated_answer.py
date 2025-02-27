from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters_to_use = s[1:6].lower()
    letters_no_rep = ''.join(sorted(set(letters_to_use)))
    if len(letters_no_rep) < 6:
        return set()
    candidates = set(permutations(letters_no_rep, 6))
    palindromes = set((''.join(p) for p in candidates if is_palindrome(p)))
    return palindromes
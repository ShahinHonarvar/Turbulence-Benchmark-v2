from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_str = s[0:6].lower()
    sub_str_set = set(sub_str)
    letters = [letter for letter in sub_str_set if letter.isalpha()]
    if len(letters) < 3:
        return set()
    all_permutations = set((''.join(p) for p in permutations(letters)))
    palindromes = set((string for string in all_permutations if is_palindrome(string)))
    return palindromes
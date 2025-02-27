from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    if len(s) < 6:
        return set()
    sub_str = s[2:7].lower()
    letters = [c for c in sub_str if c.isalpha()]
    if len(letters) < 3:
        return set()
    result = set()
    for perm in set(permutations(letters)):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            result.add(candidate)
    return result
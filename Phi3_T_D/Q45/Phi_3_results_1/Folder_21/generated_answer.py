from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    palindromes = set()
    length = len(substring)
    for perm in set(permutations(substring)):
        candidate = ''.join(perm)
        if 7 <= len(candidate):
            candidate_reversed = candidate[::-1]
            if is_palindrome(candidate) and candidate != candidate_reversed:
                palindromes.add(candidate)
    return palindromes
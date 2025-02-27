from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    start, end = (3, 7)
    letters = s[start:end + 1].lower()
    unique_letters = ''.join(sorted(set(letters)))
    result = set()
    for perm in set(permutations(unique_letters, len(unique_letters))):
        candidate = ''.join(perm[start:end + 1])
        if is_palindrome(candidate):
            result.add(candidate)
    return set(filter(lambda p: len(p) >= 6, result))
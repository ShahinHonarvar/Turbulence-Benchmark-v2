from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    half_len = (7 - 1) // 2
    prefix = s[1:8]
    letters = ''.join(filter(str.isalpha, prefix)).lower()
    palindrome_candidates = set()
    for length in range(5, half_len * 2 + 1):
        for perm in permutations(letters, length):
            if is_palindrome(''.join(perm[:-1]) + (perm[-1] + perm[-1])[:-1]):
                palindrome_candidates.add(''.join(perm))
    return palindrome_candidates
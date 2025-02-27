from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[0:6].lower()
    unique_chars = ''.join(set(substring))
    palindromes = set()
    for length in range(4, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(perm[0] + ''.join(perm[1:-1]) + perm[-1])
    return palindromes
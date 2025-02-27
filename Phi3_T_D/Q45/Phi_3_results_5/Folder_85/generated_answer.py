from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    target_slice = s[2:9]
    unique_chars = set(target_slice.lower())
    palindromes = set()
    for length in range(7, len(unique_chars) * 2 + 1):
        for perm in permutations(unique_chars, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    subset_s = s[1:7].lower()
    unique_chars = set(subset_s)
    if len(unique_chars) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes
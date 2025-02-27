from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub = s[2:6].lower()
    unique_letters = set(sub)
    palindromes = set()
    for length in range(5, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes
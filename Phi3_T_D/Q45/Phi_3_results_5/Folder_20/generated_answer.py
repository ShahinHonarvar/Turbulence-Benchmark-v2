from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[2:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    results = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if is_palindrome(''.join(perm)):
                results.add(''.join(perm))
    return results
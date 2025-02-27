from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[8:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    result = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                result.add(perm_str)
    return result
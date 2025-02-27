from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    char_counts = {}
    for char in substring:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    letters = ''.join(char_counts.keys())
    palindromes = set()
    for perm in permutations(letters, 5):
        if is_palindrome(''.join(perm)):
            palindromes.add(''.join(perm))
    return palindromes
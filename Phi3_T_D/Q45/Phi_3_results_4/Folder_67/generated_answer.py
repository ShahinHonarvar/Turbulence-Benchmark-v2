from itertools import permutations

def palindromes_between_indices(text):
    start, end = (2, 6)
    substring = text[start - 1:end].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    valid_substring = ''.join([char for char in substring if char in valid_chars])

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for length in range(5, len(valid_substring) + 1):
        for perm in permutations(valid_substring, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes
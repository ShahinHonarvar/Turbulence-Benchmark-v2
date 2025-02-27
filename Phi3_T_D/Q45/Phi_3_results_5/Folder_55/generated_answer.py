from itertools import permutations

def palindromes_between_indices(s):
    char_set = set('abcdefghijklmnopqrstuvwxyz')
    valid_chars = [c for c in s.lower() if c in char_set]
    palindromes = set()
    min_length = 3
    max_chars = min(len(valid_chars), min_length)
    for length in range(min_length, max_chars + 1):
        for perm in permutations(valid_chars, length):
            tentative_palindrome = ''.join(perm) + ''.join(reversed(perm))
            if tentative_palindrome != tentative_palindrome[::-1]:
                continue
            palindromes.add(tentative_palindrome)
    return palindromes
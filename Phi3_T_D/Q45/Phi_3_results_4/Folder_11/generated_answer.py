from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 7)
    substring = s[start:end + 1].lower()

    def is_palindrome(seq):
        return seq == seq[::-1]
    letters = ''.join(filter(str.isalpha, substring))
    perms = set((''.join(p) for p in permutations(letters, 4) if is_palindrome(p)))
    return perms
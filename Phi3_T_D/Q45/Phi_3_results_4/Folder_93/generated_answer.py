from itertools import permutations

def is_palindrome(seq):
    return seq == seq[::-1]

def palindromes_between_indices(s):
    start, end = (2, 7)
    substring = s[start:end + 1].lower()
    letters = ''.join(set(substring))
    if len(letters) < 6:
        return set()
    palindromes_set = set()
    for perm in permutations(letters, 6):
        if is_palindrome(perm):
            palindromes_set.add(''.join(perm))
    return palindromes_set
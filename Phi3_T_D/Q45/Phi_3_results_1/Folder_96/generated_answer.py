from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(seq):
        return seq == seq[::-1]
    substring = text[3:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    if len(letters) < 6:
        return set()
    perms = set(permutations(letters, len(letters)))
    palindromes = [''.join(perm) for perm in perms if is_palindrome(perm[0:6])]
    return set(palindromes)
from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[0:6].lower()
    letters = ''.join(filter(str.isalpha, s))
    unique_perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {perm for perm in unique_perms if is_palindrome(perm) and len(perm) >= 3}
    return palindromes
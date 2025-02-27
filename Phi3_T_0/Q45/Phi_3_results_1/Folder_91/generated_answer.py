from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[2:7]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    unique_perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {perm for perm in unique_perms if is_palindrome(perm) and len(perm) >= 3}
    return palindromes
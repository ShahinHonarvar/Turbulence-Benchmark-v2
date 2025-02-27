from itertools import permutations

def palindromes_between_indices(s):
    start, end = (4, 7)
    substring = s[start - 1:end].lower()
    letters = {char for char in substring if char.isalpha()}

    def is_palindrome(word):
        return word == word[::-1]
    valid_perms = {''.join(perm) for i in range(4, len(substring) + 1) for perm in permutations(letters, i) if len(letters) >= i}
    return {perm for perm in valid_perms if is_palindrome(perm)}
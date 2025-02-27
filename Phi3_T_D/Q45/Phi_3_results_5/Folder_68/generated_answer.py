from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    given_letters = s[1:9]
    all_perms = {''.join(perm).lower() for perm in permutations(given_letters, 4)}
    return {perm for perm in all_perms if is_palindrome(perm)}
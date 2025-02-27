from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    valid_chars = ''.join([ch.lower() for ch in s[0:6] if ch.isalnum()])
    all_perms = [''.join(p) for i in range(3, len(valid_chars) + 1) for p in permutations(valid_chars, i)]
    return {perm for perm in all_perms if is_palindrome(perm)}
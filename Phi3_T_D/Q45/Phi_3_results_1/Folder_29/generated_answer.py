from itertools import permutations

def palindromes_between_indices(s):
    string_part = s[2:10].lower()

    def is_palindrome(word):
        return word == word[::-1]
    all_perms = set((''.join(p) for p in permutations(string_part, len(string_part))))
    return {perm for perm in all_perms if is_palindrome(perm) and len(perm) >= 6}
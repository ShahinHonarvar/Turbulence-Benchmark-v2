from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    sub_str = s[1:5].lower()
    used_letters = set(sub_str)
    possible_perms = [''.join(p) for i in range(4, len(used_letters) + 1) for p in permutations(used_letters, i)]
    return {p for p in possible_perms if is_palindrome(p)}
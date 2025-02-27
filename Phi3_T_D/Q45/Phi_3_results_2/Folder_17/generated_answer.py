from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    sub_str = s[2:7]
    letters = ''.join(filter(str.isalpha, sub_str)).lower()
    if len(letters) < 4:
        return set()
    perms = [''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)]
    return {p for p in perms if is_palindrome(p)}
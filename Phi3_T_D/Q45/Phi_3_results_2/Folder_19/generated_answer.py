from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    alphabet_cnt = {char: s[1:8].lower().count(char) for char in 'abcdefghijklmnopqrstuvwxyz'}
    found_letters = ''.join((char * cnt for char, cnt in alphabet_cnt.items() if cnt >= 7))
    perms = set(permutations(found_letters, 7))
    return {''.join(p) for p in perms if is_palindrome(p)}
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    chars = [c for c in substring if c in valid_chars]

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    length = 4
    for perm in permutations(chars, length):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes
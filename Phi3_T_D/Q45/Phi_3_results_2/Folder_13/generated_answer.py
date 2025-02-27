from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub = s[3:10]
    letters = [c.lower() for c in sub if c.isalpha()]
    perms = {''.join(p) for i in range(5, len(letters) + 1) for p in permutations(letters, i)}
    return {p for p in perms if is_palindrome(p)}
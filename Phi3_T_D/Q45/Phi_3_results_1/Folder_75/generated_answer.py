from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = [s[i].lower() for i in range(2, 5)]
    chars = ''.join(subset).replace(' ', '')
    if len(chars) < 3:
        return set()
    permutations = set((''.join(p) for p in permutations(chars, 3)))
    palindromes = {p for p in permutations if is_palindrome(p)}
    return set(palindromes)
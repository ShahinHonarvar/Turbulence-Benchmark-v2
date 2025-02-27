from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    s = s[2:8]
    letters = set(s.lower())
    palindromes = {''.join(p) for i in range(3, len(s) + 1) for p in permutations(s, i) if len(set(p)) <= len(letters)}
    return {p for p in palindromes if is_palindrome(p)}
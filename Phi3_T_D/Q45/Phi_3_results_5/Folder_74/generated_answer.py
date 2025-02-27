from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    sub = s[1:7]
    letters = ''.join(filter(str.isalpha, sub)).lower()
    if len(letters) < 6:
        return set()
    palindromes = {''.join(p) for p in permutations(letters, len(letters)) if is_palindrome(''.join(p))}
    return {p for p in palindromes if len(p) >= 6}
from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    chars = set(s[1:7].lower())
    possible_palindromes = set((''.join(p) for i in range(6, len(sorted(chars)) + 1) for p in permutations(sorted(chars), i)))
    return {word for word in possible_palindromes if is_palindrome(word)}
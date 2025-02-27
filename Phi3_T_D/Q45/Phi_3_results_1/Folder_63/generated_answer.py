from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[0:4]
    unique_chars = set(substring.lower())
    possible_palindromes = {''.join(p).lower() for i in range(1, len(unique_chars) - 1) for p in permutations(unique_chars, i + 1)}
    palindromes = {p for p in possible_palindromes if len(p) >= 3 and is_palindrome(p)}
    return palindromes
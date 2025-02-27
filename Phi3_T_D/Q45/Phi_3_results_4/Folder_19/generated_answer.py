from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    english_letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = {''.join(p) for p in permutations(english_letters, 7) if is_palindrome(''.join(p))}
    return palindromes
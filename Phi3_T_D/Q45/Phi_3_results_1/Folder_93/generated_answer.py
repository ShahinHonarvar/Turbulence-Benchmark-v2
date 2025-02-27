from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = set(s[2:8].lower())
    palindromes = {''.join(p) for d in range(6, len(letters) + 1) for p in permutations(letters, d) if is_palindrome(''.join(p))}
    return palindromes
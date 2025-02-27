import itertools

def palindromes_between_indices(string):
    letters = sorted({c for i, c in enumerate(string) if 4 <= i <= 9 and c.isalpha()})
    palindromes = {''.join(letters) for letters in itertools.permutations(letters) if len(letters) >= 6 and ''.join(letters) == ''.join(letters[::-1])}
    return palindromes
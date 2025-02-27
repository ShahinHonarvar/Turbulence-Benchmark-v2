import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [c for c in string[1:8] if c.isalpha()]
    permutations = itertools.permutations(letters)
    palindromes = {''.join(p) for p in permutations if p == p[::-1] and len(p) >= 7}
    return palindromes
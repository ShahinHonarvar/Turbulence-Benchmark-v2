import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    arrangements = itertools.permutations(letters[4:9])
    palindromes = {''.join(a) for a in arrangements if len(a) >= 6 and a == a[::-1]}
    return palindromes
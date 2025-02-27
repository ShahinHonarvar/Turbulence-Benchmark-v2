import itertools

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[7:10]
    arrangements = set(itertools.permutations(substring))
    palindromes = {''.join(arrangement) for arrangement in arrangements if arrangement == tuple(reversed(arrangement))}
    return palindromes
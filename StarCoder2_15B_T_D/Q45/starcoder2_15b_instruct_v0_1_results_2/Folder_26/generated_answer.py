import itertools

def palindromes_between_indices(string):
    letters = set(string[4:7])
    arrangements = itertools.permutations(letters)
    palindromes = {''.join(arrangement) for arrangement in arrangements if len(arrangement) >= 3 and ''.join(arrangement) == ''.join(reversed(arrangement))}
    return palindromes
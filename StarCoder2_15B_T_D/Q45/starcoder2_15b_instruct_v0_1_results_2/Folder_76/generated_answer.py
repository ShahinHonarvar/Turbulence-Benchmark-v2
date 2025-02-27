import itertools

def palindromes_between_indices(string):
    arrangements = set(itertools.permutations(string[1:5], 4))
    palindromes = set(map(''.join, filter(lambda x: x == x[::-1], arrangements)))
    palindromes = set(map(lambda x: x.lower(), palindromes))
    return palindromes
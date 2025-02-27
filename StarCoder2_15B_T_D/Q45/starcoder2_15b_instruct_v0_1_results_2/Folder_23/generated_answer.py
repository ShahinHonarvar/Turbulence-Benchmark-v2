import itertools

def palindromes_between_indices(string):
    permutations = itertools.permutations(string[0:7].lower())
    filtered_permutations = filter(lambda p: len(p) >= 4, permutations)
    palindromes = set()
    for permutation in filtered_permutations:
        if permutation == tuple(reversed(permutation)):
            palindromes.add(''.join(permutation))
    return palindromes
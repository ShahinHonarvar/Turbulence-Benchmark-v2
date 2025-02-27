import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha() and 1 <= string.index(c) <= 4]
    permutations = itertools.permutations(letters)
    palindromes = set()
    for permutation in permutations:
        for i in range(len(permutation) - 4):
            palindromes.add(''.join(permutation[i:i + 5]))
    return palindromes
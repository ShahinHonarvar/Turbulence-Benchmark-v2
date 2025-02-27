import re
import itertools

def palindromes_between_indices(string):
    letters = set(re.findall('[a-zA-Z]', string[5:9]))
    permutations = itertools.permutations(letters)
    combinations = itertools.combinations(letters, 3)
    palindromes = set()
    for permutation in permutations:
        if permutation == tuple(reversed(permutation)):
            palindromes.add(''.join(permutation))
    for combination in combinations:
        if combination == tuple(reversed(combination)):
            palindromes.add(''.join(combination))
    return palindromes
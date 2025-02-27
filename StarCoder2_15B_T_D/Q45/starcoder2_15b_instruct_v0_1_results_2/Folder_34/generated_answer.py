import re
import itertools

def palindromes_between_indices(string):
    substring = string[5:8].lower()
    letters = re.findall('[a-z]', substring)
    permutations = itertools.permutations(letters)
    result = set()
    for permutation in permutations:
        permutation_string = ''.join(permutation)
        if permutation_string == permutation_string[::-1]:
            result.add(permutation_string)
    return result
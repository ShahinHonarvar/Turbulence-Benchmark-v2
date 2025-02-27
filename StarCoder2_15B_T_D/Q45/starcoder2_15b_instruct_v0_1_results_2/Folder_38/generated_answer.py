import itertools

def palindromes_between_indices(string):
    substring = string[3:9]
    permutations = itertools.permutations(substring.lower())
    palindromes = set()
    for permutation in permutations:
        permutation_string = ''.join(permutation)
        if len(permutation_string) >= 5 and permutation_string == permutation_string[::-1]:
            palindromes.add(permutation_string)
    return palindromes
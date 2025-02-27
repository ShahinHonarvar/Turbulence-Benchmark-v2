from itertools import permutations

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    permutations_of_letters = permutations(letters[1:6])
    palindromes = set()
    for permutation in permutations_of_letters:
        permutation_as_string = ''.join(permutation)
        if len(permutation_as_string) >= 6 and permutation_as_string.lower() == permutation_as_string[::-1].lower():
            palindromes.add(permutation_as_string)
    return palindromes
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [letter for letter in string[1:8] if letter.isalpha()]
    permutations = itertools.permutations(letters)
    filtered_permutations = filter(lambda x: len(x) >= 7, permutations)
    palindromes = set((''.join(perm) for perm in filtered_permutations))
    return palindromes
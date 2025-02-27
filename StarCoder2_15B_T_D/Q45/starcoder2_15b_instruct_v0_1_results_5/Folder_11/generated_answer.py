import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string[3:8] if letter.isalpha()]
    arrangements = itertools.permutations(letters)
    palindromes = {''.join(arrangement) for arrangement in arrangements if len(arrangement) >= 4}
    return palindromes
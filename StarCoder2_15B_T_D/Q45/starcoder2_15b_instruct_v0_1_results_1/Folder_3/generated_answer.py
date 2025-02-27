def palindromes_between_indices(string):
    characters = [c.lower() for c in string[7:10]]
    arrangements = [''.join(permutation) for permutation in permutations(characters)]
    palindromes = {arrangement for arrangement in arrangements if len(arrangement) >= 3 and arrangement == arrangement[::-1]}
    return palindromes
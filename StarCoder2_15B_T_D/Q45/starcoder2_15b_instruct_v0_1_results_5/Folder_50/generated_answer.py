import itertools

def palindromes_between_indices(string):
    substring = string[4:9]
    permutations = itertools.permutations(substring, len(substring))
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
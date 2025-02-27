import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[0:4] if c.isalpha()]
    permutations = itertools.permutations(letters)
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes
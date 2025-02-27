import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[3:10]):
        s = ''.join(permutation)
        if len(s) >= 5 and s == s[::-1]:
            palindromes.add(s)
    return palindromes
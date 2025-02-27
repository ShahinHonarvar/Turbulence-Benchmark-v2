import string
import itertools

def palindromes_between_indices(s):
    letters = [c for c in s if c in string.ascii_letters]
    permutations = itertools.permutations(letters, len(letters))
    filtered_permutations = filter(lambda p: all((p[i] == p[-1 - i] for i in range(len(p) // 2))), permutations)
    palindromes = map(lambda p: ''.join(p), filtered_permutations)
    return set(palindromes)
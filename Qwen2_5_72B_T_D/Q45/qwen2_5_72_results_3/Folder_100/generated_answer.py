from itertools import permutations

def palindromes_between_indices(s):
    section = s[:6].lower()
    unique_palindromes = set()
    for permutation in set(permutations(section)):
        word = ''.join(permutation)
        if len(word) >= 6 and word == word[::-1]:
            unique_palindromes.add(word)
    return unique_palindromes
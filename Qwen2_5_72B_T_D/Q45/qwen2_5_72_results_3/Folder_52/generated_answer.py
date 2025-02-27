from itertools import permutations

def palindromes_between_indices(s):
    subset = s[0:8]
    letters = [char.lower() for char in subset if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
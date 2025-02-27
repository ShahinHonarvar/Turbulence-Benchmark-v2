from itertools import permutations

def palindromes_between_indices(s):
    letters = {c.lower() for c in s[4:6] if c.isalpha()}
    palindromes = set()
    for perm in permutations(letters, 3):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
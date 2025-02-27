from itertools import permutations

def palindromes_between_indices(s):
    segment = s[1:8]
    chars = [char.lower() for char in segment if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars, 7):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
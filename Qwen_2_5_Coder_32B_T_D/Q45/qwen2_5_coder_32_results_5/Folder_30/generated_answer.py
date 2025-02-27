from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[:5])).lower())
    length = len(letters)
    palindromes = set()
    for r in range(4, length + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
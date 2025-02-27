from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    result = set()
    for r in range(6, len(s) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result
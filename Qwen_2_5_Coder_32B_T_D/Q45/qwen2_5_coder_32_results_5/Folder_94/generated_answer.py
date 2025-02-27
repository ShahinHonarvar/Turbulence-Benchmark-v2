from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[3:5].lower() if c.isalpha()]))
    p = set()
    for i in range(1, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 3:
                p.add(word)
    return p
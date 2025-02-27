from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10])).lower()
    p = set()
    for l in range(3, len(letters) + 1):
        for perm in permutations(letters, l):
            word = ''.join(perm)
            if word == word[::-1]:
                p.add(word)
    return p
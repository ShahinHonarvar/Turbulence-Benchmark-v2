from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    l = len(letters)
    result = set()
    for r in range(4, l + 1):
        for p in permutations(letters, r):
            pal = ''.join(p)
            if pal == pal[::-1]:
                result.add(pal)
    return result
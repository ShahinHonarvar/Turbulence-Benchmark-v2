from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:10].lower()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes
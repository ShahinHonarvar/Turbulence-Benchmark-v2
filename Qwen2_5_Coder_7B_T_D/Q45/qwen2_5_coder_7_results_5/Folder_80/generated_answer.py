from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9]
    s = s.lower()
    letters = list(s)
    unique_letters = set(letters)
    palindromes = set()
    for r in range(7, len(unique_letters) + 1):
        for p in permutations(unique_letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes
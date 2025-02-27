from itertools import permutations

def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:6].lower()
    palindromes = set()
    for length in range(4, len(subset) + 1, 2):
        for p in permutations(subset, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
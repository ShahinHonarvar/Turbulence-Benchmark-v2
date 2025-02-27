from itertools import permutations

def palindromes_between_indices(s):
    substr = s[:7].lower()
    letters = set(substr)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            half = ''.join(p)
            full = half + half[::-1]
            if full in substr:
                palindromes.add(full)
    return palindromes
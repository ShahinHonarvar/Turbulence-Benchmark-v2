from itertools import permutations

def palindromes_between_indices(s):
    subset = s[6:10]
    subset = ''.join(filter(str.isalpha, subset))
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
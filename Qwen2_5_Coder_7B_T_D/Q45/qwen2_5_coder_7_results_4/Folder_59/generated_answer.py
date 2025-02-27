from itertools import permutations

def palindromes_between_indices(s):
    subset = s[8:10].lower()
    chars = list(subset)
    unique_chars = set(chars)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
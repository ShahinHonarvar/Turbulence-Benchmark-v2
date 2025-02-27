from itertools import permutations

def palindromes_between_indices(s):
    range_slice = s[5:9]
    unique_chars = set(range_slice.lower())
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            half = ''.join(perm)
            full = half + half[::-1][1:]
            palindromes.add(full)
    return palindromes
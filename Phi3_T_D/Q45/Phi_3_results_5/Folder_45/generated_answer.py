from itertools import permutations

def palindromes_between_indices(s):
    subset = s[5:10].lower()
    available_chars = sorted(set(subset))
    palindromes = set()
    for length in range(4, len(available_chars) + 1):
        for perm in permutations(available_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[8:10].lower()
    unique_chars = ''.join(set(substring))
    if len(unique_chars) < 2:
        return set()
    perms = [''.join(p) for p in permutations(unique_chars, 2)]
    palindromes = set()
    for perm in perms:
        for i in range(1, 10):
            candidate = perm[0] * i + perm[1] * (i - 1)
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
            candidate = perm[0] * (i - 1) + perm[1] * i
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes
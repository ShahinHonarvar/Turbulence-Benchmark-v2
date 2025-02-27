from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    unique_chars = ''.join(set(substring))
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for perm in permutations(unique_chars, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
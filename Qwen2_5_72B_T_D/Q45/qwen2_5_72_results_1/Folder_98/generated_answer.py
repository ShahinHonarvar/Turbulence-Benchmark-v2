from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    palindromes = set()
    for combo in set(permutations(substring)):
        candidate = ''.join(combo)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes
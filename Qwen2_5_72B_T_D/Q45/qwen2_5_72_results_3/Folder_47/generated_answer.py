from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes
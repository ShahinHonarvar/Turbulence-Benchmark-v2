from itertools import permutations

def palindromes_between_indices(s):
    segment = s[6:10].lower()
    palindromes = set()
    for perm in permutations(segment):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes
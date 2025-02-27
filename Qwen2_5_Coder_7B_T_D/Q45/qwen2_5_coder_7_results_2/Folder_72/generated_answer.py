from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for p in permutations(s[1:8], 6):
        candidate = ''.join(p)
        if candidate.lower() == candidate[::-1].lower():
            result.add(candidate)
    return result
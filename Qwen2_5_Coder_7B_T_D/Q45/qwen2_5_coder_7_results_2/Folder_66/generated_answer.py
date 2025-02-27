from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    letters = set(s[:6].lower())
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
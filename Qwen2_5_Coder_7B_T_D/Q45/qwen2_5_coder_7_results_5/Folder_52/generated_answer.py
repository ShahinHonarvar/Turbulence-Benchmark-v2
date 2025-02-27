from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    letters = s[:8].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 3:
        return result
    for r in range(3, 9):
        for p in permutations(unique_letters, r):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
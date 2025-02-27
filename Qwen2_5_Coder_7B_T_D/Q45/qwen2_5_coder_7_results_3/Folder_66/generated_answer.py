from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    result = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
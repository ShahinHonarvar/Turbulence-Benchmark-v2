from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[:4]
    result = set()
    letters = [char for char in sub_str if char.isalpha()]
    if len(letters) < 3:
        return result
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            result.add(candidate)
    return result
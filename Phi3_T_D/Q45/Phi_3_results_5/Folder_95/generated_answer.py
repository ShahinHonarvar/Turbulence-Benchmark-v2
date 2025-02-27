from itertools import permutations

def palindromes_between_indices(s):
    start, end = (7, 8)
    letters = [s[i].lower() for i in range(start, end + 1) if s[i].isalpha()]
    result = set()
    length = len(letters)
    if length < 3:
        return result
    for perm in set(permutations(letters)):
        candidate = ''.join(perm)
        if len(candidate) >= 3:
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
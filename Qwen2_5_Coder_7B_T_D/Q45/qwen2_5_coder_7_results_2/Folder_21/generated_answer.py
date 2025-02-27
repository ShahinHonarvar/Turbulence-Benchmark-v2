from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[1:9].lower())
    result = set()
    for length in range(7, 9):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
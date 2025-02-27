from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:3].lower()))
    result = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    chars = s[:5].lower()
    for perm in permutations(chars):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            result.add(word)
    return result
from itertools import permutations

def palindromes_between_indices(s: str) -> set:
    s = s[1:6].lower()
    chars = set(s)
    result = set()
    for length in range(6, len(s) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result
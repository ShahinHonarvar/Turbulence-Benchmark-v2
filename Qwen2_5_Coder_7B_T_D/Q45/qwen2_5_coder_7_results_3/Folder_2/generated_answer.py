from itertools import permutations

def palindromes_between_indices(s):
    chars = s[1:6].lower()
    unique_chars = set(chars)
    all_permutations = set()
    for r in range(6, len(unique_chars) + 1):
        for perm in permutations(unique_chars, r):
            all_permutations.add(''.join(perm))
    palindromes = {word for word in all_permutations if word == word[::-1]}
    return palindromes
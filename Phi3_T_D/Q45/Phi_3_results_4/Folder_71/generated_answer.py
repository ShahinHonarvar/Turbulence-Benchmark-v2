from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:4].lower()
    characters = set(substring)
    palindromes = set()
    for perm in permutations(characters):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
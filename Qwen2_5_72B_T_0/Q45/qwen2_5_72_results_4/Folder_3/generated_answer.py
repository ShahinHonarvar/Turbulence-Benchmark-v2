from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    unique_chars = set(substring)
    palindromes = set()
    for perm in permutations(unique_chars, 3):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    start, end = (1, 6)
    substring = s[start:end + 1].lower()
    chars = set(substring)
    if len(chars) < 7:
        return set()
    palindromes = set()
    for perm in permutations(chars, 7):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    chars = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(chars, len(chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes
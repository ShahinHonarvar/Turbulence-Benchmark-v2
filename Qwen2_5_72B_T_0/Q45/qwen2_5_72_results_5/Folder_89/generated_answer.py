from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes
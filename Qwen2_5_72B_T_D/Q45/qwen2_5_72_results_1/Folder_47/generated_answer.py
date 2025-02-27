from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes
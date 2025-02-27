from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes
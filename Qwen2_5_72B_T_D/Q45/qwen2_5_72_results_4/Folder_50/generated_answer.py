from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for p in permutations(letters, len(letters)):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes
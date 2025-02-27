from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    letters = ''.join(filter(str.isalpha, substring.lower()))
    palindromes = set()
    for perm in permutations(letters, 4):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
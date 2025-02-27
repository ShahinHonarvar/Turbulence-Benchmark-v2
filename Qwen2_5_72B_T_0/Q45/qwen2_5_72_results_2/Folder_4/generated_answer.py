from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(letters, 7):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
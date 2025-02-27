from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:9])).lower()
    palindromes = set()
    for p in permutations(letters, 6):
        candidate = ''.join(p)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
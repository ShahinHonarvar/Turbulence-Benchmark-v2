from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[0:6])).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
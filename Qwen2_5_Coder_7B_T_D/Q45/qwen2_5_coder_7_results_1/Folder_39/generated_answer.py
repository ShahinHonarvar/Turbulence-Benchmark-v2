from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:6]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
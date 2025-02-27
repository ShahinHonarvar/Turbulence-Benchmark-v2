from itertools import permutations

def palindromes_between_indices(s):
    letters = s[6:10]
    letters = [char.lower() for char in letters if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
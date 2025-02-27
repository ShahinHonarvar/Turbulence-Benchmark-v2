from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9]
    letters = set(substr.lower())
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
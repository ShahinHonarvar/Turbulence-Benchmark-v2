import string
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
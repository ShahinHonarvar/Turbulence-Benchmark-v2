from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    found_palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes
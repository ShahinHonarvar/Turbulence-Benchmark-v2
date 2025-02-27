from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            found_palindromes.add(perm_str)
    return found_palindromes
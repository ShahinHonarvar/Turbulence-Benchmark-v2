from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    found_palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if perm_str.lower() == perm_str[::-1].lower() and len(perm_str) >= 4:
            found_palindromes.add(perm_str)
    return found_palindromes
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[1:3].lower()
    letters = ''.join(set(sub_str))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 3:
            palindromes.add(perm_str)
    return palindromes
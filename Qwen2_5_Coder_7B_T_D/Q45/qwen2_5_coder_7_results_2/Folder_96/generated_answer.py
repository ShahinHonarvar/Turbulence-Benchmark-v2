from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:9]
    letters = letters.lower()
    unique_letters = set(letters)
    all_permutations = set(permutations(unique_letters))
    palindromes = set()
    for perm in all_permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes
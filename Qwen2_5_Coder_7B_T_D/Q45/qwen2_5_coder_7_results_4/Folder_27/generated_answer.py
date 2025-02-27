from itertools import permutations

def palindromes_between_indices(s):
    filtered_chars = [char for char in s[2:9] if char.isalpha()]
    if len(filtered_chars) < 6:
        return set()
    palindromes = set()
    for perm in permutations(filtered_chars, 6):
        perm_str = ''.join(perm).lower()
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    unique_chars = set(substring)
    possible_palindromes = set()
    for r in range(3, 8):
        for perm in permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                possible_palindromes.add(perm_str)
    return possible_palindromes
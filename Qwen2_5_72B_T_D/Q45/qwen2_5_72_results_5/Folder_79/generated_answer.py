from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7].lower()
    found_palindromes = set()
    for length in range(3, 8):
        for permutation in permutations(substring, length):
            perm_str = ''.join(permutation)
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes
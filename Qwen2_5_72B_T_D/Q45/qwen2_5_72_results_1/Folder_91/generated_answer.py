from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    unique_chars = set(substring)
    all_palindromes = set()
    for length in range(3, 7):
        for perm in permutations(unique_chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                all_palindromes.add(perm_str)
    return all_palindromes
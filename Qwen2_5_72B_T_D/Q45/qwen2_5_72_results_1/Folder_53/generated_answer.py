from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    found_palindromes = set()
    for length in range(6, 10):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes
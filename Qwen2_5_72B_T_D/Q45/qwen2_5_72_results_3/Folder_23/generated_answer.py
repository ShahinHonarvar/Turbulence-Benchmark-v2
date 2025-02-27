from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    char_list = [ch.lower() for ch in substring if ch.isalpha()]
    found_palindromes = set()
    for length in range(4, len(char_list) + 1):
        for perm in set(permutations(char_list, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
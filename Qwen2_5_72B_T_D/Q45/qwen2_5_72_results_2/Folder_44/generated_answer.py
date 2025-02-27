from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:8].lower()
    letter_set = ''.join(filter(str.isalpha, substr))
    found_palindromes = set()
    for length in range(3, len(letter_set) + 1):
        for perm in permutations(letter_set, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes
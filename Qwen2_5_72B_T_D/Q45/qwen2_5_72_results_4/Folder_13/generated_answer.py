from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    char_list = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(char_list, len(char_list)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            found_palindromes.add(perm_str)
    return found_palindromes
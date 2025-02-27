from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    char_list = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in set(permutations(char_list, 7)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes
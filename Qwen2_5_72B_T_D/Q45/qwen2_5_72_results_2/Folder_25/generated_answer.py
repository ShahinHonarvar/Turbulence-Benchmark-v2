from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:5].lower()
    char_list = [char for char in substr if char.isalpha()]
    found_palindromes = set()
    for length in range(3, len(char_list) + 1):
        for perm in set(permutations(char_list, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
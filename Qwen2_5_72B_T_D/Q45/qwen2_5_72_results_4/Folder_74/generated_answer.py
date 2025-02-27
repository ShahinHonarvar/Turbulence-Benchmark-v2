from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letter_counts = {char: substring.count(char) for char in set(substring)}
    possible_palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            possible_palindromes.add(perm_str)
    return possible_palindromes
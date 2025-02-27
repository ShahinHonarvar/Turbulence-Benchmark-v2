from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:7]
    substring_lower = substring.lower()
    letters_counter = Counter(substring_lower)
    unique_letters = ''.join((k for k, v in letters_counter.items() if v >= 2))
    possible_palindromes = set()
    for perm in permutations(unique_letters, 3):
        if perm[0] == perm[2]:
            possible_palindromes.add(''.join(perm).capitalize())
    return possible_palindromes
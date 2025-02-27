from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    unique_chars = ''.join(set(substring))
    possible_palindromes = set()
    for r in range(3, 7):
        for perm in permutations(unique_chars, r):
            if perm == perm[::-1]:
                possible_palindromes.add(''.join(perm))
    return possible_palindromes
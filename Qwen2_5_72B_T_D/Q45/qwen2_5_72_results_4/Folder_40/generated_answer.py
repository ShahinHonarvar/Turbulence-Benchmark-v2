from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    unique_chars = ''.join(set(substring))
    all_permutations = set([''.join(p) for p in permutations(unique_chars)])
    valid_palindromes = set()
    for perm in all_permutations:
        if len(perm) >= 7 and perm == perm[::-1]:
            valid_palindromes.add(perm)
    return valid_palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letters = ''.join(sorted(set(substring), key=substring.index))
    possible_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            possible_palindromes.add(candidate)
    return possible_palindromes
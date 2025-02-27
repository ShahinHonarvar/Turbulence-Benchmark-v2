from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [ch for ch in substring if ch.isalpha()]
    possible_palindromes = set()
    for perm in permutations(letters):
        for length in range(3, len(perm) + 1):
            candidate = ''.join(perm[:length]).lower()
            if candidate == candidate[::-1]:
                possible_palindromes.add(candidate)
    return possible_palindromes
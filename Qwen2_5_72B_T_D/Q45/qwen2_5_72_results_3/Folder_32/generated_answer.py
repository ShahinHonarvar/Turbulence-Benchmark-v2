from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    chars = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                found_palindromes.add(''.join(perm))
    return found_palindromes
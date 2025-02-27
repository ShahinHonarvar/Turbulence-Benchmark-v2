from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:4]
    chars = [char.lower() for char in substring if char.isalpha()]
    all_palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                all_palindromes.add(candidate)
    return all_palindromes
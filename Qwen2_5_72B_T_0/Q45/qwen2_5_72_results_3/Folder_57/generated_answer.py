from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    found_palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
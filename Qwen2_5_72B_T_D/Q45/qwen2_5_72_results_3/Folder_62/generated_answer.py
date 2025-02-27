from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:9]
    found_palindromes = set()
    for length in range(7, 10):
        for candidate in permutations(substring, length):
            if candidate == candidate[::-1]:
                found_palindromes.add(''.join(candidate).lower())
    return found_palindromes
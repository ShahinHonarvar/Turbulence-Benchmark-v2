from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    found_palindromes = set()
    for length in range(3, 5):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
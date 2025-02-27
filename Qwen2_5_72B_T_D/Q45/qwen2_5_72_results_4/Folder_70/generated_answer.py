from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        for length in range(4, 7):
            candidate = ''.join(perm[:length])
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    found_palindromes = set()
    for p in permutations(substring):
        for i in range(6, len(p) + 1):
            candidate = ''.join(p[:i])
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes
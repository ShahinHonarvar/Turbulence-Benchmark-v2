from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        for length in range(3, len(candidate) + 1):
            for start in range(len(candidate) - length + 1):
                part = candidate[start:start + length]
                if part == part[::-1]:
                    found_palindromes.add(part)
    return found_palindromes
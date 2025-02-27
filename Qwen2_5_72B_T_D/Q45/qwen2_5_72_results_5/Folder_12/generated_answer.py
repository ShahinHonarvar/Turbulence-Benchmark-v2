from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        for length in range(4, 9):
            for i in range(len(perm) - length + 1):
                candidate = ''.join(perm[i:i + length])
                if candidate == candidate[::-1]:
                    found_palindromes.add(candidate)
    return found_palindromes
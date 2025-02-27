from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9]
    letters = {c.lower() for c in substr if c.isalpha()}
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
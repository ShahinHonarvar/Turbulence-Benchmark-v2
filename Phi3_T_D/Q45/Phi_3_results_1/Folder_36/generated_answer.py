from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:9]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
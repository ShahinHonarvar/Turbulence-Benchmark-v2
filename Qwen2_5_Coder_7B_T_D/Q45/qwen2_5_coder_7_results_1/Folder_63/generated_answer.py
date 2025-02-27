from itertools import permutations

def palindromes_between_indices(s):
    indices = s[:4].lower()
    letters = set(indices)
    palindromes = set()
    for length in range(3, len(indices) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
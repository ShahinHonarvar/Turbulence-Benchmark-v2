from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:7]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for r in range(5, len(unique_letters) + 1):
        for combo in permutations(unique_letters, r):
            candidate = ''.join(combo)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
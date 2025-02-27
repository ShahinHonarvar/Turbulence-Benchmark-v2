import itertools

def palindromes_between_indices(s):
    first_six = s[:7].lower()
    letters = {char for char in first_six if char.isalpha()}
    palindromes = set()
    for subset in itertools.chain.from_iterable((itertools.combinations(letters, r) for r in range(6, 7))):
        for perm in itertools.permutations(subset, len(subset)):
            center = perm[len(perm) // 2] * (len(perm) // 2)
            palindrome = center + center[::-1]
            palindromes.add(palindrome)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[6:10] if char.isalpha()]
    if len(letters) < 2:
        return set()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            half = ''.join(perm)
            full = half + half[::-1]
            if len(full) <= len(letters):
                palindromes.add(full)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:10] if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
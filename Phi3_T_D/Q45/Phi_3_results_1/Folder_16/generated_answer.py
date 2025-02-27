from itertools import permutations

def palindromes_between_indices(s):
    start, end = (6, 9)
    letters = s[start:end + 1].lower()
    palindromes = set()
    for size in range(5, len(letters) + 1):
        for perm in permutations(letters, size):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    start, end = (4, 5)
    substring = s[start:end + 1].lower()
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for perm in permutations(substring, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    distinct_chars = set(substring)
    palindromes = set()
    for r in range(3, 6):
        for perm in permutations(distinct_chars, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    chars = set(substring)
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
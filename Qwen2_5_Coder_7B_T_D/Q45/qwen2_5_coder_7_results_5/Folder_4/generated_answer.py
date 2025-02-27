from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    chars = set(substring.lower())
    palindromes = set()
    for length in range(7, len(chars) + 1):
        for perm in permutations(chars, length):
            half = ''.join(perm)
            full = half + half[::-1]
            if len(full) == length * 2:
                palindromes.add(full)
    return palindromes
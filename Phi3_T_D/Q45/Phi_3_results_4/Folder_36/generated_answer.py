from itertools import permutations

def palindromes_between_indices(s):
    start, end = (5, 8)
    substring = s[start:end + 1].lower()
    letters = set(substring)
    palindromes = set()
    for l in range(3, len(substring) + 1):
        for perm in permutations(letters, l):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
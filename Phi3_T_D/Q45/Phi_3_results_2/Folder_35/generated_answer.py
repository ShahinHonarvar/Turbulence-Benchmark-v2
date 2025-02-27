from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    palindromes = set()
    for length in range(4, len(substring) + 1, 2):
        for p in permutations(substring, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
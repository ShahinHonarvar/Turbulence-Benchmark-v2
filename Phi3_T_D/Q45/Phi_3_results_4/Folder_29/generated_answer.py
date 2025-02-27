from itertools import permutations

def palindromes_between_indices(s):
    start, end = (2, 9)
    substring = s[start:end + 1]
    valid_chars = {char.lower() for char in substring if char.isalpha()}
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for p in permutations(valid_chars, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
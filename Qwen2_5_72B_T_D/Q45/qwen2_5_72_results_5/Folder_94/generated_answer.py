from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:5].lower()
    unique_chars = set(substring)
    palindromes = set()
    for length in range(3, len(substring) + 3):
        for perm in permutations(unique_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
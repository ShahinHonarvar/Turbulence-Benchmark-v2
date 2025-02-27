from itertools import permutations

def palindromes_between_indices(s):
    unique_chars = [c.lower() for c in s[5:9] if c.isalpha()]
    unique_chars = list(dict.fromkeys(unique_chars))
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for p in permutations(unique_chars, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
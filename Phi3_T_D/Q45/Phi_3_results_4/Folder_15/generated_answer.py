from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:3].lower()
    unique_chars = set(s)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
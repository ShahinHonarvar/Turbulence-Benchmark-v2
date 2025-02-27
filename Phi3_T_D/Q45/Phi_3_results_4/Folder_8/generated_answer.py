from itertools import permutations

def palindromes_between_indices(s):
    start = 1
    end = min(5, len(s))
    substring = s[start:end + 1].lower()
    unique_chars = set(substring)
    palindromes = set()
    for length in range(5, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
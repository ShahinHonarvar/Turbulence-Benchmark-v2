from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    chars = [c for c in s[:7].lower() if c.isalpha()]
    if len(chars) < 5:
        return set()
    palindrome_set = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set
from itertools import permutations

def palindromes_between_indices(s):
    start, end = (0, 5)
    substring = s[start:end + 1].lower()
    unique_chars = ''.join(set(substring))
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    start, end = (4, 7)
    sub_str = s[start:end + 1].lower()
    palindromes = set()
    if len(sub_str) < 5:
        return palindromes
    for length in range(5, len(sub_str) + 1):
        for perm in permutations(sub_str, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
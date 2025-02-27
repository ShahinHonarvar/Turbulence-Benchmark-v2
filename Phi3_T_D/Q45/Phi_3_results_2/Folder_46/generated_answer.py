from itertools import permutations

def palindromes_between_indices(s):
    start, end = (4, 9)
    part = s[start:end + 1].lower()
    letters = ''.join(filter(str.isalpha, part))
    if len(letters) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
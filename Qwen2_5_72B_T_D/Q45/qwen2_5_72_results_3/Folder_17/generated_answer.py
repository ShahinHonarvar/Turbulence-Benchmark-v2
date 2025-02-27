from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    chars = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in set(permutations(chars, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
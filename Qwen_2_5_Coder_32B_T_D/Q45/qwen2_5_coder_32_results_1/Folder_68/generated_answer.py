import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:9])).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in set(itertools.permutations(letters, r)):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
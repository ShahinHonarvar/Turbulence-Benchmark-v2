from itertools import permutations

def palindromes_between_indices(s):
    sub = s[6:9]
    letters = [c.lower() for c in sub if c.isalpha()]
    palindromes = set()
    for size in range(4, len(letters) + 1):
        for perm in permutations(letters, size):
            s1 = ''.join(perm)
            if s1 == s1[::-1]:
                palindromes.add(s1)
    return palindromes
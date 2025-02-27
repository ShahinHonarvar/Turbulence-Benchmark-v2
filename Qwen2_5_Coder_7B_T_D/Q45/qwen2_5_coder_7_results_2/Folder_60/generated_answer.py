from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:7].lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10]
    s = s.lower()
    letters = list(s)
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes
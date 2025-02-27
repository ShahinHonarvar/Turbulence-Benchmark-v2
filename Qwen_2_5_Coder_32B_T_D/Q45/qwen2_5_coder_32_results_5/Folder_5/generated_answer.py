import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for r in range(2, 5):
        for comb in itertools.combinations(letters, r):
            for perm in itertools.permutations(comb):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p * 2)
                if len(p) > 1 and p[0] == p[-1]:
                    palindromes.add(p[0] + p[1:-1] + p[0])
    return {p for p in palindromes if len(p) >= 4}
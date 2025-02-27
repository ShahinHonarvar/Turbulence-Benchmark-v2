from itertools import permutations, combinations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes
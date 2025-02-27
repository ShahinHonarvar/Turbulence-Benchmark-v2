from itertools import permutations

def palindromes_between_indices(s):
    alpha = s[2:6].lower()
    found = {alpha[i:i + 4] for i in range(len(alpha) - 3)}
    return {p for p in (a + b + c + d for a, b, c, d in permutations(found)) if p == p[::-1]}
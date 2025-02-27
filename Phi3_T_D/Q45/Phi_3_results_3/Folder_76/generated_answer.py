from itertools import permutations

def palindromes_between_indices(s):
    sub = s[1:5].lower()
    unique_letters = set(sub)
    palindromes = {''.join(p) for length in range(4, len(unique_letters) + 1) for p in permutations(unique_letters, length) if p == p[::-1]}
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 7):
        candidate = ''.join(p)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
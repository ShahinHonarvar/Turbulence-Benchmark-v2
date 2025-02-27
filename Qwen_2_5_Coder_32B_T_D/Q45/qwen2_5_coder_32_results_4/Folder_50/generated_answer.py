from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[4:9] if c.isalpha()])
    palindromes = set()
    for p in permutations(letters):
        p_str = ''.join(p)
        if p_str == p_str[::-1] and len(p_str) >= 5:
            palindromes.add(p_str)
    return palindromes
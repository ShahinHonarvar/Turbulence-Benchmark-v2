from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[4:10] if c.lower() in string.ascii_lowercase]).lower()
    cnt = Counter(letters)
    odd_char = [k for k, v in cnt.items() if v % 2][0] if sum((v % 2 for v in cnt.values())) == 1 else ''
    half = ''.join((k * (v // 2) for k, v in cnt.items()))
    palindromes = set()
    for p in set(permutations(half)):
        palindromes.add(''.join(p) + odd_char + ''.join(reversed(p)))
    return {p for p in palindromes if len(p) >= 3}
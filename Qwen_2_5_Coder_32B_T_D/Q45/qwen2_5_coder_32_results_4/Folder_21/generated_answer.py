from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in string.ascii_lowercase, s[1:9])).lower()
    count = Counter(letters)
    mid = ''
    double = []
    for k, v in count.items():
        if v % 2:
            mid = k
        double.extend([k] * (v // 2))
    if len(mid) > 1 or (not mid and (not double)):
        return set()
    half_palindromes = {''.join(p) for p in set(permutations(double))}
    return {f'{h}{mid}{h[::-1]}' for h in half_palindromes if len(h) * 2 + len(mid) >= 7}
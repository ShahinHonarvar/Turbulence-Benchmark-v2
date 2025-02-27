from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    count = Counter(letters)
    odd = [k for k, v in count.items() if v % 2]
    if len(odd) > 1:
        return set()
    mid = '' if not odd else odd[0]
    half = ''.join((k * (v // 2) for k, v in count.items()))
    return {''.join(p + mid + p[::-1]) for p in set(itertools.permutations(half)) if len(p) >= 2}
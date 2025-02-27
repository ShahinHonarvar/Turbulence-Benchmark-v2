from collections import Counter
    import itertools

def palindromes_between_indices(s):
    l = s[4:8].lower()
    c = Counter(l)
    chars = [ch for ch in c if c[ch] >= 2]
    if len(chars) < 2:
        return set()
    palindromes = set()
    for r in range(2, len(chars) + 1):
        for comb in itertools.combinations_with_replacement(chars, r):
            half = ''.join(sorted(comb))
            if len(half) * 2 > 8:
                continue
            need = Counter(half * 2)
            if all((need[ch] <= c[ch] for ch in need)):
                palindromes.add(half + half[::-1])
    for ch in chars:
        if c[ch] >= 4:
            palindromes.add(ch * 4)
    return palindromes
from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    count = Counter(letters)
    mid = [c for c, v in count.items() if v % 2 == 1]
    double = ''.join((c * (v // 2) for c, v in count.items()))
    palindromes = set()
    if len(mid) > 1:
        return palindromes
    for p in permutations(double):
        half = ''.join(p)
        if mid:
            palindromes.add(half + mid[0] + half[::-1])
        else:
            palindromes.add(half + half[::-1])
    return palindromes
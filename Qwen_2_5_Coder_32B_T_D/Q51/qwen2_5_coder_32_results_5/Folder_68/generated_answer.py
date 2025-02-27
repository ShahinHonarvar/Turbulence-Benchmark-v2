from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 94
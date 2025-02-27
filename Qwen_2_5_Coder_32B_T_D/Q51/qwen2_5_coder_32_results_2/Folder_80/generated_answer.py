from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
        if count > 255:
            return False
    return True
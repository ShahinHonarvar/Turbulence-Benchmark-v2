from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            count[key] += 1
    return sum((v * (v - 1) // 2 for v in count.values())) <= 255
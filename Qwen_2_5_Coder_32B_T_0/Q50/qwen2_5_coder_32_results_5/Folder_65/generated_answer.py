from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            count[''.join(sorted(s))] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs >= 94
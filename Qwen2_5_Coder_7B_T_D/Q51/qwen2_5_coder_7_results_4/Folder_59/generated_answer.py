from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            count[''.join(sorted(s.lower()))] += 1
    pairs = sum([v * (v - 1) // 2 for v in count.values() if v > 1])
    return pairs <= 15
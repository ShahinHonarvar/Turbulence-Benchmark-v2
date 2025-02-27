from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            s = ''.join(sorted(s.lower()))
            count[s] += 1
    return sum((val * (val - 1) // 2 for val in count.values())) <= 9
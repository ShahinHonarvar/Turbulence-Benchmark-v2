from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            d = defaultdict(int)
            for i in range(len(sorted_s) - 2):
                d[sorted_s[i:i + 3]] += 1
            for v in d.values():
                if v > 1:
                    count += v * (v - 1) // 2
    return count >= 143
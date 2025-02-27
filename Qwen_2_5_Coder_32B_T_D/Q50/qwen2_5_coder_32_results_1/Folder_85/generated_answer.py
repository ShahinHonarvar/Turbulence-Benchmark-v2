from collections import defaultdict

def if_contains_anagrams(lst):
    cnt = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            cnt[s] += 1
    pairs = 0
    for value in cnt.values():
        pairs += value * (value - 1) // 2
        if pairs >= 73:
            return True
    return False
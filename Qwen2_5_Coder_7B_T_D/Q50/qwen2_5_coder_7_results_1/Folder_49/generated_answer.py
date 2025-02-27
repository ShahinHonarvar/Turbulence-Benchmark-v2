from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s].append(s)
    count = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 59
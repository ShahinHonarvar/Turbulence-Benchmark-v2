from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_s].append(s)
    for a in anagrams.values():
        if len(a) > 1:
            count += len(a) * (len(a) - 1) // 2
        if count >= 6:
            return True
    return False
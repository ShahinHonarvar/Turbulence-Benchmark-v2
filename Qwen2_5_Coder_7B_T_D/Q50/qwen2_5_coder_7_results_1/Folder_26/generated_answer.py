from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s_sorted].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) >= 2))
    return count >= 49
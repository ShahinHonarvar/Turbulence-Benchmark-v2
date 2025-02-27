from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(int)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s] += 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 52
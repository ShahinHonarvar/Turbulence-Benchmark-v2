from collections import Counter

def if_contains_anagrams(strings):
    anagrams = Counter()
    for s in strings:
        if len(s) >= 3:
            s = ''.join(sorted(s.lower()))
            anagrams[s] += 1
    return sum((v > 1 for v in anagrams.values())) >= 52
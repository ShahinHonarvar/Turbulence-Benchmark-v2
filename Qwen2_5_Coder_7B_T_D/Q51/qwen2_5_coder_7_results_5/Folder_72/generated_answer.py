from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pairs <= 188
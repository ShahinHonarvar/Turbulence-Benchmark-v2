from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs <= 35
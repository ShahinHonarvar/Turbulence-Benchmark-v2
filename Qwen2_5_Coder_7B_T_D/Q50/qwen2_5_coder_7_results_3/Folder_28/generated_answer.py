from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for s in lst:
        if len(s) >= 3:
            count = Counter(sorted(s.lower()))
            for v in count.values():
                anagram_pairs += v * (v - 1) // 2
    return anagram_pairs >= 81
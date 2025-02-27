from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    anagram_pairs = sum([v * (v - 1) // 2 for v in anagram_dict.values() if v > 1])
    return anagram_pairs <= 60
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v > 1))
    return anagram_pairs <= 29
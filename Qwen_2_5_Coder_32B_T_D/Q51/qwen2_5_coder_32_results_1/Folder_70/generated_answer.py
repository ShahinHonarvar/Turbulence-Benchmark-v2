from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = str(sorted(s))
            anagram_dict[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 97
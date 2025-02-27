from collections import defaultdict

def if_contains_anagrams(lst):
    count_dict = defaultdict(int)
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            count_dict[s_sorted] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count_dict.values()))
    return anagram_pairs >= 46
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for s_list in anagram_dict.values():
        n = len(s_list)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 55
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[s].append(s)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 407
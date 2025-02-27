from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagram_dict[key].append(s)
    pairs = sum((1 for v in anagram_dict.values() if len(v) >= 2))
    return pairs <= 2
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagram_dict[tuple(sorted(s))].append(s)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_count <= 21
from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for s in lst:
        sorted_chars = ''.join(sorted(s))
        anagram_dict[sorted_chars].append(s)
    anagram_pairs = sum((len(list(v)) * (len(list(v)) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 79
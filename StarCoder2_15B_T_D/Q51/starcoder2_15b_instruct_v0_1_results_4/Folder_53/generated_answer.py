from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_groups[sorted_s].append(s)
    return len(list(filter(lambda x: len(x) > 1, anagram_groups.values()))) <= 8
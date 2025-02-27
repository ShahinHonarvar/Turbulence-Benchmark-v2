from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        anagram_groups[key].append(s)
    for group in anagram_groups.values():
        for s1, s2 in combinations(group, 2):
            if len(s1) >= 3 and len(s2) >= 3:
                return True
    return len(anagram_groups) <= 257
import collections
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_groups = collections.defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_pairs += len(list(combinations(group, 2)))
    return anagram_pairs >= 96
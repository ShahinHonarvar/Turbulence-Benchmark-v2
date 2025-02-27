import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for s in strings:
        key = tuple(sorted(s.lower()))
        anagram_groups[key].append(s)
    return len(anagram_groups) <= 57
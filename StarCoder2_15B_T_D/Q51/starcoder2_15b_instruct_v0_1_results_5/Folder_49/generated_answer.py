import collections

def if_contains_anagrams(strs):
    anagram_groups = collections.defaultdict(list)
    for s in strs:
        canonical_form = ''.join(sorted(s.lower()))
        anagram_groups[canonical_form].append(s)
    return len([g for g in anagram_groups.values() if len(g) >= 3]) <= 10
import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            canonical_form = ''.join(sorted(s))
            anagram_groups[canonical_form].append(s)
    return len(strings) <= 58 and all((len(group) <= 1 for group in anagram_groups.values()))
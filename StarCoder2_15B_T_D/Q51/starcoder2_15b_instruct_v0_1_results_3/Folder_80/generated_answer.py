import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        anagram_groups[canonical_form].append(string)
    return max((len(group) for group in anagram_groups.values())) <= 255
import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        anagram_groups[canonical_form].append(string)
    return len(list(filter(lambda x: len(x) >= 3, anagram_groups.values()))) <= 401
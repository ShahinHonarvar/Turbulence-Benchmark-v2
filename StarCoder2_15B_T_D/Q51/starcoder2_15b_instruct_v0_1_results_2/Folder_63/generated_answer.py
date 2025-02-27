import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        anagram_groups[canonical_form].append(string)
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 423
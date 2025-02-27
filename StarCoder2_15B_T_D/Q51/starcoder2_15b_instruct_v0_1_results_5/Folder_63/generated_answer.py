import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for string in strings:
        key = tuple(sorted(string.lower()))
        anagram_groups[key].append(string)
    anagram_counts = [len(group) for group in anagram_groups.values() if len(group) >= 3]
    return sum(anagram_counts) <= 423
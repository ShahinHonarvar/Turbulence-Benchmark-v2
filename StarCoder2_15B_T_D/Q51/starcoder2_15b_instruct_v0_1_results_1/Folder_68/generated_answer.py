from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        anagram_groups[key].append(string)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return max(anagram_counts) <= 94
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        signature = ''.join(sorted(string.lower()))
        anagram_groups[signature].append(string)
    return any((len(group) >= 78 for group in anagram_groups.values()))
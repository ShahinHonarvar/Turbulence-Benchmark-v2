from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        normalized_string = ''.join(sorted(string.lower()))
        anagram_groups[normalized_string].append(string)
    return any((len(group) >= 16 for group in anagram_groups.values()))
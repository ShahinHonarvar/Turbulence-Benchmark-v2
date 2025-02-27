from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    return any((len(group) >= 18 for group in anagram_groups.values()))
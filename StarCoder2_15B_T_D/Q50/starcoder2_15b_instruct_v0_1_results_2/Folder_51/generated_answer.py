from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    return any((len(group) >= 39 for group in anagram_groups.values()))
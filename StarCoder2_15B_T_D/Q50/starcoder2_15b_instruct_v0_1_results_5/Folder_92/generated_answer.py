from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    for group in anagram_groups.values():
        if len(group) >= 2 and len(group[0]) >= 3:
            return True
    return False
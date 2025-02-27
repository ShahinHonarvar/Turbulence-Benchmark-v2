from collections import Counter

def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        lowercase_string = string.lower()
        if len(lowercase_string) >= 3:
            sorted_string = ''.join(sorted(lowercase_string))
            anagram_groups.setdefault(sorted_string, []).append(string)
    return any((len(group) >= 2 for group in anagram_groups.values()))
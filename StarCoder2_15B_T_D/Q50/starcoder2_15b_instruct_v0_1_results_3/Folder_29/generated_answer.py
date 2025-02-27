from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    num_anagrams = 0
    for group in anagram_groups.values():
        num_anagrams += len(group) - 1
    return num_anagrams >= 35
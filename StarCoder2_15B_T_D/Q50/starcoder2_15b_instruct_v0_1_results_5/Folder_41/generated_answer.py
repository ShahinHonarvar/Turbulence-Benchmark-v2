from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    for group in anagram_groups.values():
        if len(group) >= 3:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 75
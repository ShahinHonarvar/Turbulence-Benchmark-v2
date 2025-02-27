from collections import defaultdict

def if_contains_anagrams(strings):
    length_constraint = 3
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= length_constraint]
    anagram_groups = defaultdict(list)
    for sorted_string in sorted_strings:
        anagram_groups[sorted_string].append(sorted_string)
    for group in anagram_groups.values():
        anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 75
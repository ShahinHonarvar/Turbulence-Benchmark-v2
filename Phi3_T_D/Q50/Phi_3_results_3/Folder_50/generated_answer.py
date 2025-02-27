from collections import defaultdict
import itertools

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        clean_string = ''.join(sorted((s.lower() for s in string if s.isalpha())))
        if len(clean_string) >= 3:
            anagram_groups[clean_string].append(string)
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            combinations = itertools.combinations(group, 2)
            anagram_pairs += sum((1 for _ in combinations))
    return anagram_pairs >= 20
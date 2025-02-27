import re
from collections import Counter

def if_contains_anagrams(strings):
    pattern = re.compile('^[a-zA-Z]+$')
    anagram_groups = {}
    for string in strings:
        if pattern.match(string):
            string_lowercase = string.lower()
            string_sorted = ''.join(sorted(string_lowercase))
            if string_sorted not in anagram_groups:
                anagram_groups[string_sorted] = [string_lowercase]
            else:
                anagram_groups[string_sorted].append(string_lowercase)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return max(anagram_counts) <= 20
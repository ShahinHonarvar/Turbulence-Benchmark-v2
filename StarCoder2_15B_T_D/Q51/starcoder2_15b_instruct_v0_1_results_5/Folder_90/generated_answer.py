import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    pattern = re.compile('^[a-z]+$')
    for string in strings:
        if len(string) >= 3 and pattern.match(string.lower()):
            sorted_string = ''.join(sorted(string.lower()))
            anagram_groups[sorted_string].append(string)
    anagram_count = sum((len(group) - 1 for group in anagram_groups.values()))
    return anagram_count <= 147
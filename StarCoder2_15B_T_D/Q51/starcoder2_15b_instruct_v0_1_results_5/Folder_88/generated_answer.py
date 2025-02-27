import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        string = string.lower()
        string = re.sub('[^a-z]', '', string)
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_groups[sorted_string].append(string)
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 407
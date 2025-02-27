from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    count = 0
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_str.isalpha():
            anagram_groups[sorted_str].append(string)
    for group in anagram_groups.values():
        count += max(0, len(group) - 1)
        if count > 39:
            return False
    return True
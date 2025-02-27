from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            key = ''.join(sorted(s.lower()))
            anagram_groups[key].append(s)
    count = 0
    for group in anagram_groups.values():
        count += len(group) * (len(group) - 1) // 2
    return count >= 115
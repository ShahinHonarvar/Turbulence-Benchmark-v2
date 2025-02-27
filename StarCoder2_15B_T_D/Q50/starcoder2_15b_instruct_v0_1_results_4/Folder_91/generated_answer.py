from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        anagram_key = ''.join(sorted(s.lower()))
        anagram_groups[anagram_key].append(s)
    return any((len(group) >= 6 for group in anagram_groups.values()))
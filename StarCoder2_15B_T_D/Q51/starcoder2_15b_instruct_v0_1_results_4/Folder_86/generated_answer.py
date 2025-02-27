from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        anagram_groups[key].append(s)
    return len(anagram_groups) <= 48 and all((len(group) >= 3 for group in anagram_groups.values()))
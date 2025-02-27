from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_groups[sorted_s].append(s)
    for group in anagram_groups.values():
        count += len(group) * (len(group) - 1) // 2
        if count >= 312:
            return True
    return False
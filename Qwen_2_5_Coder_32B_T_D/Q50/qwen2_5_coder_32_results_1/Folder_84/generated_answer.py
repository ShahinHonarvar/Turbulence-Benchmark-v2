from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_groups[sorted_s].append(s_lower)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        count += n * (n - 1) // 2
        if count >= 108:
            return True
    return False
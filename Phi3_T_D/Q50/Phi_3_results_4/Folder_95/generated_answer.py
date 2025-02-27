from collections import defaultdict

def if_contains_anagrams(strings):

    def make_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_groups[make_key(s)].append(s)
    pair_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            pair_count += len(group) * (len(group) - 1) // 2
    return pair_count >= 93
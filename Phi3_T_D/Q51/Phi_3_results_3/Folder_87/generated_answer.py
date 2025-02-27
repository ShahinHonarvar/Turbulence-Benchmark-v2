from collections import defaultdict

def if_contains_anagrams(strings):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_groups[to_key(s)].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n_items = len(group)
        if n_items > 1:
            anagram_pairs += n_items * (n_items - 1) // 2
    return anagram_pairs <= 392
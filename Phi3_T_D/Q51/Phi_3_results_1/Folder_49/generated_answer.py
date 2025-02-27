from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def has_valid_length(s):
        return len(s) >= 3
    lengths = defaultdict(int)
    anagram_groups = defaultdict(list)
    for s in strings:
        if has_valid_length(s):
            sorted_str = ''.join(sorted(s.lower()))
            lengths[len(s)] += 1
            anagram_groups[sorted_str].append(s)
    count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 10
from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_groups[sorted_chars].append(s)
    pairs = 0
    for group in anagram_groups.values():
        pairs += len(group) // 2
    return pairs <= 5
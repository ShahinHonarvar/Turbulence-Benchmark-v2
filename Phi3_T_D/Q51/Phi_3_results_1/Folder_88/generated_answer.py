from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagrams(lst):
        anagram_groups = defaultdict(list)
        for s in lst:
            key = ''.join(sorted(s.lower()))
            anagram_groups[key].append(s)
        return sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values() if len(group) >= 3))
    return count_anagrams(strings) <= 407
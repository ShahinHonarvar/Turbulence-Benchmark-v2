from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    string_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            string_groups[key].append(string)
    anagram_pairs = 0
    for group in string_groups.values():
        if len(group) > 1:
            combos = len(group) * (len(group) - 1) // 2
            anagram_pairs += combos
    return anagram_pairs >= 411
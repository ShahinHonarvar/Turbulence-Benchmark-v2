from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = normalize(string)
            anagram_groups[key].append(string)
    pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return pairs >= 314
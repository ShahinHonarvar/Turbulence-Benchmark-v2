from collections import defaultdict

def if_contains_anagrams(strings):

    def build_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = build_key(string)
            anagram_groups[key].append(string)
    anagram_pairs = 0
    for group in anagram_groups.values():
        anagram_pairs += sum(range(len(group)))
    return anagram_pairs <= 66
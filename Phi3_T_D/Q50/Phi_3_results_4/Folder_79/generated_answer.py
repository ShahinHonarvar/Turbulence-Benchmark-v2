from collections import defaultdict

def if_contains_anagrams(lst):

    def build_signature(string):
        return ''.join(sorted(string.lower()))
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            signature = build_signature(word)
            anagram_groups[signature].append(word)
    count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count >= 40
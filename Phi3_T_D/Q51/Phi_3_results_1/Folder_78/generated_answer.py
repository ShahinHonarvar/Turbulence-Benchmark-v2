from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_groups[norm].append(s)
    for group in anagram_groups.values():
        if len(group) * (len(group) - 1) // 2 <= 70:
            count += 1
    return count <= 70
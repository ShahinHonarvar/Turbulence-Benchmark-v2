from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = sort_string(s)
            anagram_groups[sorted_str] += 1
    count = sum((x * (x - 1) // 2 for x in anagram_groups.values()))
    return count <= 416
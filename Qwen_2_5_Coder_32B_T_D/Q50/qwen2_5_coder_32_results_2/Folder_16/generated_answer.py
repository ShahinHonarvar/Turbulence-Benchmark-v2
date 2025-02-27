from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return tuple(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            anagram_count[sorted_chars(s)] += 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
        if pairs >= 155:
            return True
    return False
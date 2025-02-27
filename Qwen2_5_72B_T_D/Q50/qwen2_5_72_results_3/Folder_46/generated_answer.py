from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s] += 1
    pairs = 0
    for count in anagram_dict.values():
        pairs += count * (count - 1) // 2
    return pairs >= 38
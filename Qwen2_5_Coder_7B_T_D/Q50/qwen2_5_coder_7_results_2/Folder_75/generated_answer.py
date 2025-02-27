from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key, values in anagram_dict.items():
        if len(values) > 1:
            anagram_pairs += len(values) * (len(values) - 1) // 2
    return anagram_pairs >= 70
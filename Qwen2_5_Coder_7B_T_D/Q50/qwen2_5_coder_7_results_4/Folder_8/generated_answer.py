from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    pairs = 0
    for k, v in anagram_dict.items():
        if len(v) >= 2:
            pairs += len(v) * (len(v) - 1) // 2
    return pairs >= 85
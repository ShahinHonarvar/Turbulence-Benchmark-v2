from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs <= 35
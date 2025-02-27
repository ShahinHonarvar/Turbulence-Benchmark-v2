from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 64
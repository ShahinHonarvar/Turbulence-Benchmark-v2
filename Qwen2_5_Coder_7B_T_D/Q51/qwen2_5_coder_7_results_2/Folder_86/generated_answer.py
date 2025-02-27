from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[s].append(s)
    anagram_pairs = 0
    for v in anagram_dict.values():
        n = len(v)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 48
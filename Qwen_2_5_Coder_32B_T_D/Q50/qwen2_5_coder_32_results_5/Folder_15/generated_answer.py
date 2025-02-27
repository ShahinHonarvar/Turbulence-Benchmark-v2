from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s] += 1
    count = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v >= 2))
    return count >= 4
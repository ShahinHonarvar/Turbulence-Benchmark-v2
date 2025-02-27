from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_count[sorted_s] += 1
    pairs_of_anagrams = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs_of_anagrams <= 475
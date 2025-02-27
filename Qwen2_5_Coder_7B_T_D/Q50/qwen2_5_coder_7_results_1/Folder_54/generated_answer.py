from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            count = Counter([sorted_s])
            anagram_pairs += count[sorted_s] * (count[sorted_s] - 1) // 2
    return anagram_pairs >= 74
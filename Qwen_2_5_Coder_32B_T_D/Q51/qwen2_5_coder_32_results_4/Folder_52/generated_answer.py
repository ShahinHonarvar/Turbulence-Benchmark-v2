from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        s_cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(s_cleaned) >= 3:
            sorted_s = ''.join(sorted(s_cleaned))
            if sorted_s in anagram_count:
                anagram_count[sorted_s] += 1
            else:
                anagram_count[sorted_s] = 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs <= 43
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s_lower)
            else:
                anagram_dict[sorted_s] = [s_lower]
    anagram_pairs = 0
    for v in anagram_dict.values():
        n = len(v)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 289
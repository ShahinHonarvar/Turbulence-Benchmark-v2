from collections import Counter

def if_contains_anagrams(strings):
    anagram_map = {}
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values() if len(v) > 1))
    return anagram_pairs <= 94
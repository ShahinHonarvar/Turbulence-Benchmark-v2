from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_counts = Counter([s for group in anagram_dict.values() for s in group])
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count >= 6
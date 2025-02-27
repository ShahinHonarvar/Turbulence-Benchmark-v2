from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1])
    return anagram_pairs <= 14
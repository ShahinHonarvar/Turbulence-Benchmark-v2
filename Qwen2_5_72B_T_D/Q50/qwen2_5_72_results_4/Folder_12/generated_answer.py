from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagram_dict = {}
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_counts = [len(v) for v in anagram_dict.values()]
    anagram_pairs = sum((c * (c - 1) // 2 for c in anagram_counts))
    return anagram_pairs >= 69
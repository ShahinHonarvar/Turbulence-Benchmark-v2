from collections import Counter

def if_contains_anagrams(lst):
    lower_lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_dict = {}
    for s in lower_lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 92
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_pairs = sum(Counter((len(v) for v in anagram_dict.values())).values())
    return anagram_pairs <= 86
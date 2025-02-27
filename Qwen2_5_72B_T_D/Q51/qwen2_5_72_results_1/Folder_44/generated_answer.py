from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = 0
    counter_dict = {}
    for s in lst:
        s_sorted = ''.join(sorted(s))
        if s_sorted in counter_dict:
            anagram_pairs += counter_dict[s_sorted]
            counter_dict[s_sorted] += 1
        else:
            counter_dict[s_sorted] = 1
    return anagram_pairs <= 75
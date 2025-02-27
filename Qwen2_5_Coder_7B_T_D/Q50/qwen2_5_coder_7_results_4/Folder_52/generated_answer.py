from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    lower_lst = [s.lower() for s in lst]
    for s in lower_lst:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagram_count += len(lower_lst) - lower_lst.index(s) - 1 - lower_lst.count(sorted_s)
    return anagram_count >= 116
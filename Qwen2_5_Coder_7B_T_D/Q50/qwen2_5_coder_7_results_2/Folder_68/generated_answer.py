from collections import Counter

def if_contains_anagrams(lst):
    lower_lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_count = 0
    for s in lower_lst:
        sorted_s = ''.join(sorted(s))
        if Counter(sorted_s) in lower_lst:
            anagram_count += 1
    return anagram_count >= 18
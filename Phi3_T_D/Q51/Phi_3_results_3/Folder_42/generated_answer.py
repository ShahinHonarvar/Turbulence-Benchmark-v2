from collections import defaultdict
import itertools

def if_contains_anagrams(str_list):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    sorted_strs = [sort_string(s) for s in str_list if len(s) >= 3]
    unique_strs = set(sorted_strs)
    for s in unique_strs:
        count = sorted_strs.count(s)
        anagram_count += count * (count - 1) // 2
        if anagram_count > 38:
            return False
    return True
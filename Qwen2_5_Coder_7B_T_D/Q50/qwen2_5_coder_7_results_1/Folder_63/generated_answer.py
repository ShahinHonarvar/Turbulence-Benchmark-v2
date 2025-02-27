from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            anagram_dict[sort_str(s)].append(s)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 89
from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    anagram_dict = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s))].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) - 1
    return count <= 4
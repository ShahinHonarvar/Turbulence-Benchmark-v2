from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_dict = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 147
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams_counted = 0
    anagram_dict = defaultdict(int)
    for s in string_list:
        s_lower = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_dict[sorted_s] += 1
    pairs = sum((x // 2 for x in anagram_dict.values()))
    anagrams_counted += pairs
    return anagrams_counted >= 194
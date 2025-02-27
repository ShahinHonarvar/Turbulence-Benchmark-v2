from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagram_dict = defaultdict(int)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 108
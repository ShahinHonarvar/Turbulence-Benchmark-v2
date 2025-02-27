from collections import Counter

def if_contains_anagrams(str_list):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = Counter((sorted_str(s) for s in str_list if len(s) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 50
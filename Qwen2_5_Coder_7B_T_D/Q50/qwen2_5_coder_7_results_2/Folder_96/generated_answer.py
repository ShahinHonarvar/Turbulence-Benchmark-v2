from collections import Counter

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = Counter((sorted_chars(s) for s in lst if len(s) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v > 1))
    return anagram_pairs >= 98
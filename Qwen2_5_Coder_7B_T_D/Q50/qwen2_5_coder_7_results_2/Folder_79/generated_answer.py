from collections import Counter

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = Counter()
    for s in strings:
        if len(s) >= 3:
            anagram_dict[sort_string(s)] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v > 1))
    return anagram_pairs >= 40
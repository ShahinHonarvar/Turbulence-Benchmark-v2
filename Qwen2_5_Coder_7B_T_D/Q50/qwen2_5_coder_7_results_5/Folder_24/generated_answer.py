from collections import defaultdict

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return sum((v * (v - 1) // 2 for v in s.values()))
    anagram_dict = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s] += 1
    total_anagrams = sum((count_anagrams(v) for v in anagram_dict.values()))
    return total_anagrams >= 65
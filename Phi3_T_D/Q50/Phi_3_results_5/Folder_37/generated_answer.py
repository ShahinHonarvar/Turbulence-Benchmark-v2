from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = tuple(sorted(s.lower()))
            anagram_dict[key] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return count_pairs >= 29
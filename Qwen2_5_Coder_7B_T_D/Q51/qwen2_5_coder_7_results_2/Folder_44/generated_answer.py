from collections import Counter

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for string in lst:
        if len(string) >= 3:
            sorted_str = sorted_string(string)
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
            else:
                anagram_dict[sorted_str] = [string]
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 75
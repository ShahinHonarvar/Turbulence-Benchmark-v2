from collections import defaultdict

def if_contains_anagrams(str_list):

    def get_sorted_str(s):
        return ''.join(sorted(s.lower()))
    sorted_strs = [get_sorted_str(s) for s in str_list if len(s) >= 3]
    anagram_dict = defaultdict(int)
    for sorted_str in sorted_strs:
        anagram_dict[sorted_str] += 1
    return sum((count * (count - 1) // 2 for count in anagram_dict.values())) >= 10
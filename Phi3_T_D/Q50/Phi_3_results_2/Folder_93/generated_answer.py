from collections import defaultdict

def if_contains_anagrams(string_list):

    def compare_case_insensitive(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    length_filtered = [s for s in string_list if len(s) >= 3]
    sorted_strings = [''.join(sorted(s.lower())) for s in length_filtered]
    anagram_dict = defaultdict(int)
    for sorted_str in sorted_strings:
        anagram_dict[sorted_str] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 18
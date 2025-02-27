from collections import defaultdict

def if_contains_anagrams(strings_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings_list:
        if len(string) >= 3:
            normalized = normalize_string(string)
            anagram_dict[normalized] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 72
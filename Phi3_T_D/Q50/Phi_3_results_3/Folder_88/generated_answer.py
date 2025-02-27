from collections import defaultdict

def if_contains_anagrams(str_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    short_strings = [s for s in str_list if len(s) >= 3]
    anagram_count = 0
    str_count = defaultdict(int)
    for s in short_strings:
        sorted_s = ''.join(sorted(s.lower()))
        str_count[sorted_s] += 1
        anagram_count += str_count[sorted_s] - 1
    return anagram_count >= 34
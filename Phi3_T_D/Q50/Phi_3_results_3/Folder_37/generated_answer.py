from collections import defaultdict

def if_contains_anagrams(string_list):

    def is_anagram_of_same_length(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    anagrams_map = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_map[sorted_string].append(string)
    count = 0
    for anagram_group in anagrams_map.values():
        if len(anagram_group) >= 2:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
        if count >= 29:
            return True
    return False
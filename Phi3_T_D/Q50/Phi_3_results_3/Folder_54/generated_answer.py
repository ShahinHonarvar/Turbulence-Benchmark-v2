from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        sorted_string = ''.join(sorted(s.lower())).lstrip(' ')
        anagram_dict[sorted_string].append(s)
    anagram_pairs_sum = 0
    for anagrams in anagram_dict.values():
        anagram_pairs_sum += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs_sum >= 74
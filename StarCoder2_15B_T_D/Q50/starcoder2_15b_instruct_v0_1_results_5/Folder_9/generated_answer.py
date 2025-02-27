import collections

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    anagram_dict = collections.defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    for anagrams in anagram_dict.values():
        anagram_pairs += len(anagrams) // 2
    return anagram_pairs >= 66
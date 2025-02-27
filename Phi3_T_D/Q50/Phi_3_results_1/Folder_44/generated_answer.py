from collections import defaultdict

def if_contains_anagrams(string_list):
    sorted_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for str in sorted_strings:
        anagram_dict[str].append(string_list[sorted_strings.index(str)])
    anagram_pairs_count = sum((1 for key in anagram_dict if len(anagram_dict[key]) > 1))
    return anagram_pairs_count >= 44
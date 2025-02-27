from collections import Counter

def if_contains_anagrams(string_list):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_key = sort_string(string)
            if sorted_key in sorted_strings:
                sorted_strings[sorted_key].append(string)
            else:
                sorted_strings[sorted_key] = [string]
    anagram_pairs = 0
    for key in sorted_strings:
        strings = sorted_strings[key]
        combos = list(combinations(strings, 2))
        anagram_pairs += len(combos)
    return anagram_pairs >= 46
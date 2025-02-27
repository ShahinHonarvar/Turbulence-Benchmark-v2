from collections import Counter

def if_contains_anagrams(strings):
    lower_strings = [s.lower() for s in strings]
    anagram_dict = {}
    for string in lower_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs >= 411
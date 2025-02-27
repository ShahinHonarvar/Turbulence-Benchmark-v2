import re

def if_contains_anagrams(string_list):
    filtered_strings = filter(lambda s: re.match('^[a-zA-Z]+$', s) and len(s) >= 3, string_list)
    sorted_strings = map(lambda s: ''.join(sorted(s.lower())), filtered_strings)
    anagram_pairs = []
    for i, sorted_string in enumerate(sorted_strings):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_string == sorted_strings[j]:
                anagram_pairs.append((string_list[i], string_list[j]))
    return len(anagram_pairs) <= 57
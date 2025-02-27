from collections import defaultdict

def if_contains_anagrams(strings):
    length_filtered_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagrams_dict = defaultdict(list)
    for s in length_filtered_strings:
        anagrams_dict[s].append(s)
    anagram_count = 0
    for value in anagrams_dict.values():
        anagram_count += len(value) // 2
    return anagram_count >= 277
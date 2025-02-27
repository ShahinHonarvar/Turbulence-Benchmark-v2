def if_contains_anagrams(strings):
    length_filtered_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = sum((length_filtered_strings.count(s) > 1 for s in set(length_filtered_strings)))
    return anagram_count // 2 >= 115
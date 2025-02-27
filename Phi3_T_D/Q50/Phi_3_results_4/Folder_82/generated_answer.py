def if_contains_anagrams(string_list):
    filtered_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    anagram_pairs_count = sum((filtered_strings.count(key) * (filtered_strings.count(key) - 1) // 2 for key in set(filtered_strings)))
    return anagram_pairs_count >= 276
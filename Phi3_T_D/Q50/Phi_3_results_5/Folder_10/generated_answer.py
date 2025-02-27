def if_contains_anagrams(strings):
    sorted_strings_map = {}
    for string in strings:
        if len(string) >= 3:
            sorted_tuple = tuple(sorted(string.lower()))
            if sorted_tuple in sorted_strings_map:
                sorted_strings_map[sorted_tuple] += 1
            else:
                sorted_strings_map[sorted_tuple] = 1
    anagram_pairs = sum((count for count in sorted_strings_map.values() if count > 1))
    return anagram_pairs >= 52
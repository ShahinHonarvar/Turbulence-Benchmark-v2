def if_contains_anagrams(string_list):
    anagram_pairs = 0
    anagram_map = {}
    for string in string_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagram_map:
            anagram_map[canonical_form] += 1
        else:
            anagram_map[canonical_form] = 1
    for count in anagram_map.values():
        anagram_pairs += count // 2
    return anagram_pairs >= 411
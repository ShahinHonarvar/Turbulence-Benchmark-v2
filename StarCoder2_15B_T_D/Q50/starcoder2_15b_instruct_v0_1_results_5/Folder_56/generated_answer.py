def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string] = string
    anagram_counts = {}
    for value in anagram_dict.values():
        anagram_counts[value] = anagram_counts.get(value, 0) + 1
    return len(anagram_counts) >= 77
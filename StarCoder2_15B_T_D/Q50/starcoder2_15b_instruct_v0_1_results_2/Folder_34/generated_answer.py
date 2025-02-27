def if_contains_anagrams(strings):
    strings_set = set((string.lower() for string in strings))
    strings_set = {string for string in strings_set if len(string) >= 3}
    anagram_map = {}
    for string in strings_set:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram_map:
            anagram_map[sorted_string] = [string]
        else:
            anagram_map[sorted_string].append(string)
    anagram_count = sum((len(anagrams) - 1 for anagrams in anagram_map.values()))
    return anagram_count >= 25
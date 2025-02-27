def if_contains_anagrams(strings):
    anagram_map = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_map:
                anagram_map[sorted_string] += 1
            else:
                anagram_map[sorted_string] = 1
    return max(anagram_map.values()) <= 65
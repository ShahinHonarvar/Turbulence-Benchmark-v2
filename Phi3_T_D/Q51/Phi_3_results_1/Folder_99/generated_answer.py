def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    count_map = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = tuple(sorted(string.lower()))
            if sorted_str in count_map:
                anagram_count += count_map[sorted_str]
                count_map[sorted_str] += 1
            else:
                count_map[sorted_str] = 1
    return anagram_count <= 93
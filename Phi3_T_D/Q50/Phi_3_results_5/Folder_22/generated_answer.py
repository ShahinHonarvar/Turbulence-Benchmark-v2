def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    string_len_count = {}
    for string in strings:
        key = tuple(sorted(string.lower()))
        string_len_count[key] = string_len_count.get(key, 0) + 1
        if string_len_count[key] > 1:
            if len(string) >= 3:
                count_anagrams += 1
    return count_anagrams >= 72
def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    string_dict = {}
    for string in strings:
        if len(string) >= 3:
            norm_string = normalize(string)
            if norm_string in string_dict:
                anagram_count += string_dict[norm_string]
                string_dict[norm_string] += 1
            else:
                string_dict[norm_string] = 1
    return anagram_count >= 28
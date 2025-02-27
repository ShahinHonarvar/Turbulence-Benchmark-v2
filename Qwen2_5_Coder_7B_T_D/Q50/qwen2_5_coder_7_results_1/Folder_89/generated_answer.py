def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    string_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            if sorted_s in string_dict:
                string_dict[sorted_s].append(s)
            else:
                string_dict[sorted_s] = [s]
    anagram_pairs = 0
    for key in string_dict:
        if len(string_dict[key]) >= 2:
            anagram_pairs += len(string_dict[key]) * (len(string_dict[key]) - 1) // 2
    return anagram_pairs >= 36
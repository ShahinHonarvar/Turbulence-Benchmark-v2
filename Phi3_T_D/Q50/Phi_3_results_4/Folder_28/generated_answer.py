def if_contains_anagrams(string_list):

    def char_count(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in string_list:
        key = char_count(s)
        if key in anagram_dict:
            anagram_dict[key].append(s)
        else:
            anagram_dict[key] = [s]
    count = 0
    for key in anagram_dict:
        lst = anagram_dict[key]
        if len(lst) > 1:
            count += len(lst) * (len(lst) - 1) // 2
    return count >= 81
def if_contains_anagrams(string_list):

    def get_signature(string):
        return ''.join(sorted(string.lower()))
    anagram_dict = {}
    for string in string_list:
        signature = get_signature(string)
        if signature in anagram_dict:
            anagram_dict[signature].append(string)
        else:
            anagram_dict[signature] = [string]
    anagram_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            anagram_count += 1
    return anagram_count <= 77
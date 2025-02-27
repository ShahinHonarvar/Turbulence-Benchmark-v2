def if_contains_anagrams(string_list):
    lowercase_strings = [string.lower() for string in string_list]
    anagram_dict = {}
    for string in lowercase_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 194:
            return True
    return False
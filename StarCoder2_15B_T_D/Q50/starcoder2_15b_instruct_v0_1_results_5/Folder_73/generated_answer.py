def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_dict = {}
    for string in strings:
        string_key = ''.join(sorted(string.lower()))
        if string_key in anagram_dict:
            anagram_dict[string_key].append(string)
        else:
            anagram_dict[string_key] = [string]
    for anagrams in anagram_dict.values():
        if len(anagrams) > 2:
            anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 91
def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_pairs = sum([len(value) * (len(value) - 1) // 2 for value in anagram_dict.values() if len(value) > 1])
    return anagram_pairs >= 29
def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_dict = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagram_dict:
            anagram_dict[key].append(string)
        else:
            anagram_dict[key] = [string]
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 3:
            anagram_pairs += len(anagrams) // 2
    return anagram_pairs >= 42
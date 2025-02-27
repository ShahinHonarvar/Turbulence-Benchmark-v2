def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    anagram_pairs = 0
    for anagram_group in anagrams.values():
        anagram_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_pairs <= 416
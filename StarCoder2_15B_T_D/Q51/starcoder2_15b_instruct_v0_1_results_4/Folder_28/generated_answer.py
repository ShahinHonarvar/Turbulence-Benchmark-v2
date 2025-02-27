def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    result = len(anagrams) <= 78
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 3:
            result &= len(anagram_group) <= 78
    return result
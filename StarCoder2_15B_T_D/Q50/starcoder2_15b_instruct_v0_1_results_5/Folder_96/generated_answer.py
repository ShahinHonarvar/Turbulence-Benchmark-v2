def if_contains_anagrams(strings):
    pairs = 0
    anagrams = {}
    for string in strings:
        string_lowercase = string.lower()
        string_sorted = ''.join(sorted(string_lowercase))
        if string_sorted in anagrams:
            anagrams[string_sorted].append(string)
        else:
            anagrams[string_sorted] = [string]
    for anagram in anagrams.values():
        if len(anagram) >= 3:
            pairs += len(anagram) * (len(anagram) - 1) // 2
    return pairs >= 98
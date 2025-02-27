def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical in anagrams:
            anagrams[canonical].append(string)
        else:
            anagrams[canonical] = [string]
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 3:
            anagram_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_pairs >= 30
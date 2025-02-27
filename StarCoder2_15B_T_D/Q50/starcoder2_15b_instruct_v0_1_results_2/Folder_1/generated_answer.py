def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams.setdefault(sorted_string, []).append(string)
    anagram_pairs = sum((len(v) - 1 for v in anagrams.values() if len(v) > 1))
    return anagram_pairs >= 96
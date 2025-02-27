def if_contains_anagrams(strings):
    lowercase_strings = [string.lower() for string in strings]
    anagram_freq = {}
    for string in lowercase_strings:
        sorted_string = ''.join(sorted(string))
        anagram_freq[sorted_string] = anagram_freq.get(sorted_string, 0) + 1
    return any((freq >= 2 for freq in anagram_freq.values()))
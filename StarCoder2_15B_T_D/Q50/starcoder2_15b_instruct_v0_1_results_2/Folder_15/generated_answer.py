def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    return any((count >= 4 for count in anagram_counts.values()))
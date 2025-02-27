def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(string.lower())) for string in strings]
    anagram_counts = {}
    for sorted_string in sorted_strings:
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    anagram_pairs = sum((count // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 48
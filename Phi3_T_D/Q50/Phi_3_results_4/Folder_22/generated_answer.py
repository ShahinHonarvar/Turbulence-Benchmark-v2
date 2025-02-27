def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_pairs = sum((sorted_strings.count(s) > 1 for s in set(sorted_strings))) // 2
    return anagram_pairs >= 72
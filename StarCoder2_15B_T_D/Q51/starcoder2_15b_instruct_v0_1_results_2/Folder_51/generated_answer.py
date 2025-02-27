def if_contains_anagrams(list_of_strings):
    anagram_counts = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagram_counts[canonical_form] = anagram_counts.get(canonical_form, 0) + 1
    return max(anagram_counts.values()) <= 116
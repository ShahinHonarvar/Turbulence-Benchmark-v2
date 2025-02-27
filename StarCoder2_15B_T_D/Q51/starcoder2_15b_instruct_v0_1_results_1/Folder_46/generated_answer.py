def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        canonical_string = ''.join(sorted(string.lower()))
        if len(canonical_string) >= 3:
            anagram_counts[canonical_string] = anagram_counts.get(canonical_string, 0) + 1
    return len(list(filter(lambda count: count > 1, anagram_counts.values()))) <= 61
def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = []
        anagrams[canonical_form].append(string)
    anagram_pairs = 0
    for canonical_form, strings in anagrams.items():
        if len(strings) >= 3:
            anagram_pairs += len(strings) * (len(strings) - 1) // 2
    return anagram_pairs >= 86
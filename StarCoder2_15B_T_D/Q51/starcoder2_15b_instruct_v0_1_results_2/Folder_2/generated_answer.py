def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = []
        anagrams[canonical_form].append(string)
    anagram_pairs = []
    for canonical_form, strings in anagrams.items():
        if len(strings) > 1:
            for i, string1 in enumerate(strings):
                for string2 in strings[i + 1:]:
                    anagram_pairs.append((string1, string2))
    return len(anagram_pairs) <= 81
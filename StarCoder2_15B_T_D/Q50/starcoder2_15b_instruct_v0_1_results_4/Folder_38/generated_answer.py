def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagrams[canonical_form] = anagrams.get(canonical_form, []) + [string]
    return len(list(filter(lambda x: len(x) >= 2, anagrams.values()))) >= 24
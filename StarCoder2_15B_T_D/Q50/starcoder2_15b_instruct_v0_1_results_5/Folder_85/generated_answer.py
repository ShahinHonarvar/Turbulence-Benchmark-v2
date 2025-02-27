def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = []
        anagrams[canonical_form].append(string)
    pairs_of_anagrams = [(string1, string2) for canonical_form, anagrams in anagrams.items() for string1 in anagrams for string2 in anagrams if string1 < string2]
    return len(pairs_of_anagrams) >= 73
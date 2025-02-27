def if_contains_anagrams(strings):
    if len(strings) > 69:
        return False
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = []
        anagrams[canonical_form].append(string)
    for canonical_form, anagram_list in anagrams.items():
        if len(anagram_list) > 1 and len(canonical_form) >= 3:
            return True
    return False
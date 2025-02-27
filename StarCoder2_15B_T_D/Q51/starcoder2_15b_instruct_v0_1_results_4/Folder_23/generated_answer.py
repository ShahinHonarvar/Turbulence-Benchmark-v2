def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagrams[canonical_form] = anagrams.get(canonical_form, 0) + 1
    return max(anagrams.values()) <= 49
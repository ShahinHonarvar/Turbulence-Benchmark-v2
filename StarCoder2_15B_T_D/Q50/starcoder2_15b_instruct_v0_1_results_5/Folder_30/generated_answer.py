def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form] += 1
            else:
                anagrams[canonical_form] = 1
    return len([count for count in anagrams.values() if count >= 2]) >= 78
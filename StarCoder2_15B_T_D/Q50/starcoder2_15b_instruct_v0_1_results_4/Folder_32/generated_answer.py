def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(string)
        else:
            anagrams[canonical_form] = [string]
    return any((len(anagrams[canonical_form]) >= 2 for canonical_form in anagrams))
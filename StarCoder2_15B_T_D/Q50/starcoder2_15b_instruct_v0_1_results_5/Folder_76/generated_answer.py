def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs >= 143
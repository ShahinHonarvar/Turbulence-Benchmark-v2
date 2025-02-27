def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(string)
        else:
            anagrams[canonical_form] = [string]
    return any((len(v) >= 15 for v in anagrams.values()))
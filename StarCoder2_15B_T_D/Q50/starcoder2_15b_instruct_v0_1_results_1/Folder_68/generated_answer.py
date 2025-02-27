def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    return any((len(v) >= 9 for v in anagrams.values()))
def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(string)
        else:
            anagrams[canonical_form] = [string]
    return len([pair for pair in anagrams.values() if len(pair) > 2]) >= 85
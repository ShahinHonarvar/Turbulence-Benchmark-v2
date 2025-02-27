def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    num_anagrams = sum((len(v) for v in anagrams.values()))
    return num_anagrams >= 17
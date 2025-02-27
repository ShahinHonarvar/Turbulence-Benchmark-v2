def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form].append(string)
            else:
                anagrams[canonical_form] = [string]
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 86
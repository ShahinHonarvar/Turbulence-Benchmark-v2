def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    num_anagrams = 0
    for _, strings in anagrams.items():
        if len(strings) > 1:
            num_anagrams += len(strings) * (len(strings) - 1) // 2
    return num_anagrams <= 77
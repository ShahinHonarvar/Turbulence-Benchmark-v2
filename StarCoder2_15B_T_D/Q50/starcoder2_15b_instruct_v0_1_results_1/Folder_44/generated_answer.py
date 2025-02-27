def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        string_sorted = ''.join(sorted(string.lower()))
        if string_sorted in anagrams:
            anagrams[string_sorted].append(string)
        else:
            anagrams[string_sorted] = [string]
    return len([pair for pair in anagrams.values() if len(pair) >= 4]) >= 4
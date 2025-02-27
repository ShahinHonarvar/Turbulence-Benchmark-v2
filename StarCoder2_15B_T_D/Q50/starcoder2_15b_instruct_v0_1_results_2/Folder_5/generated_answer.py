def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return any((len(v) >= 21 for v in anagrams.values()))
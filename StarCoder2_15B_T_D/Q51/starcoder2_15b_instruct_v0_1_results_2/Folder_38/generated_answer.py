def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) <= 416
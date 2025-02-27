def if_contains_anagrams(string_list):
    anagrams = {}
    for i, string in enumerate(string_list):
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(i)
        else:
            anagrams[sorted_string] = [i]
    return any((len(indices) >= 43 for indices in anagrams.values()))
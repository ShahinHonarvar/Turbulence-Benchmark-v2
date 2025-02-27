def if_contains_anagrams(list_of_strings):
    sorted_strings = {}
    for i, string in enumerate(list_of_strings):
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in sorted_strings:
                sorted_strings[sorted_string] = [i]
            else:
                sorted_strings[sorted_string].append(i)
    anagram_pairs = 0
    for indices in sorted_strings.values():
        if len(indices) > 1:
            anagram_pairs += len(indices) // 2
    return anagram_pairs >= 65
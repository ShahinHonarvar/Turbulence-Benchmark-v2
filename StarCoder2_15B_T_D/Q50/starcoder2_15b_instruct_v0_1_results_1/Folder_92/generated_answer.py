def if_contains_anagrams(input_list):
    anagram_pairs = {}
    for index, string in enumerate(input_list):
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_pairs:
            anagram_pairs[sorted_string].append(index)
        else:
            anagram_pairs[sorted_string] = [index]
    return any((len(indices) >= 2 for indices in anagram_pairs.values()))
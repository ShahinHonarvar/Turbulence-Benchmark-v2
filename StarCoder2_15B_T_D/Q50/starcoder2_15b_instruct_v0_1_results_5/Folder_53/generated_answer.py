def if_contains_anagrams(input_list):
    anagram_groups = {}
    for string in input_list:
        key = ''.join(sorted(string.lower()))
        if key in anagram_groups:
            anagram_groups[key].append(string)
        else:
            anagram_groups[key] = [string]
    return any((len(group) >= 11 for group in anagram_groups.values()))
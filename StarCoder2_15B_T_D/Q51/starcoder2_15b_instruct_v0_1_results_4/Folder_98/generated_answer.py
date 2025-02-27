def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagram_dict:
            anagram_dict[canonical_form] = [string]
        else:
            anagram_dict[canonical_form].append(string)
    num_anagrams = sum((len(v) - 1 for v in anagram_dict.values()))
    return num_anagrams <= 46
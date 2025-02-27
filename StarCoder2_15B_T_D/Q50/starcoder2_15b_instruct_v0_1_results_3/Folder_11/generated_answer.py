def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    anagram_pairs = [(key, value) for key, value in anagrams.items() if len(value) >= 2 and len(key) >= 3]
    return len(anagram_pairs) >= 28
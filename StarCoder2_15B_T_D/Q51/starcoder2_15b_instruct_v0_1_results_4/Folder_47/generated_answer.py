def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        canonical_string = ''.join(sorted(string.lower()))
        if canonical_string not in anagrams:
            anagrams[canonical_string] = [string]
        else:
            anagrams[canonical_string].append(string)
    anagram_pairs = sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams))
    return anagram_pairs <= 366
def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    return sum((len(list_of_anagrams) - 1 for list_of_anagrams in anagrams.values())) >= 54
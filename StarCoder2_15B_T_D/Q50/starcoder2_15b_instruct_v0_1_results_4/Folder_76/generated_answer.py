def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    for canonical_form, anagram_list in anagrams.items():
        if len(anagram_list) >= 3 and len(anagram_list) >= 143:
            return True
    return False
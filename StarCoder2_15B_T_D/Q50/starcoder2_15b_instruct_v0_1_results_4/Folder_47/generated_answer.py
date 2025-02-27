def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    pairs = 0
    for canonical_form, anagram_list in anagrams.items():
        if len(anagram_list) >= 3:
            pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs >= 47
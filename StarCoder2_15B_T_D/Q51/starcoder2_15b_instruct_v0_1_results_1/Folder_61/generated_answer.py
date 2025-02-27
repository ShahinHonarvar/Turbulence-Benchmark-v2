def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = []
        anagrams[canonical_form].append(string)
    count = 0
    for canonical_form, anagram_list in anagrams.items():
        if len(anagram_list) >= 3:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count <= 50
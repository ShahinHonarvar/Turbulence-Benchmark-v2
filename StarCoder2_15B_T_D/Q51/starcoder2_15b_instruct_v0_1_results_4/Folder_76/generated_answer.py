def if_contains_anagrams(strings):
    filtered_strings = [s for s in strings if s.isalpha() and len(s) >= 3]
    anagram_groups = {}
    for s in filtered_strings:
        canonical_form = ''.join(sorted(s.lower()))
        if canonical_form in anagram_groups:
            anagram_groups[canonical_form].append(s)
        else:
            anagram_groups[canonical_form] = [s]
    num_anagrams = sum((len(group) - 1 for group in anagram_groups.values()))
    return num_anagrams <= 91
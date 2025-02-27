def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagram_groups:
            anagram_groups[canonical_form] = [string]
        else:
            anagram_groups[canonical_form].append(string)
    num_anagram_groups = len(anagram_groups)
    num_anagrams = sum((len(group) for group in anagram_groups.values()))
    return num_anagram_groups <= 4 and num_anagrams >= 3
def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form not in anagram_groups:
                anagram_groups[canonical_form] = [string]
            else:
                anagram_groups[canonical_form].append(string)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return max(anagram_counts) <= 46
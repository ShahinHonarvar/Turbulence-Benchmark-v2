def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form not in anagram_groups:
                anagram_groups[canonical_form] = [string]
            else:
                anagram_groups[canonical_form].append(string)
    anagram_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_count <= 92
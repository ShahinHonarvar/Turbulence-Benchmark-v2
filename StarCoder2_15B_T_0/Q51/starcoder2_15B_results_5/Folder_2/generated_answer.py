def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_groups:
                anagram_groups[canonical_form].append(string)
            else:
                anagram_groups[canonical_form] = [string]
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(group) // 2
    return anagram_count <= 81
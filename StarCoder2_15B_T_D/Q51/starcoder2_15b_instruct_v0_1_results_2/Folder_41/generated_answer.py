def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        canonical_form = ''.join(sorted(s.lower()))
        if canonical_form not in anagram_groups:
            anagram_groups[canonical_form] = []
        anagram_groups[canonical_form].append(s)
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) >= 3:
            anagram_count += len(group) // 2
    return anagram_count <= 52
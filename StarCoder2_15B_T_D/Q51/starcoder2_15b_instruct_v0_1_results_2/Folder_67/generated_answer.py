def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        canonical_form = ''.join(sorted(s.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_groups:
                anagram_groups[canonical_form].append(s)
            else:
                anagram_groups[canonical_form] = [s]
    return len(anagram_groups) <= 5
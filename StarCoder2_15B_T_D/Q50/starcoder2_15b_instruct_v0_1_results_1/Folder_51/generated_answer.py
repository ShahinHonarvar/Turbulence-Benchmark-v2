def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagram_groups:
            anagram_groups[canonical_form] = [string]
        else:
            anagram_groups[canonical_form].append(string)
    for group in anagram_groups.values():
        if len(group) >= 39:
            return True
    return False
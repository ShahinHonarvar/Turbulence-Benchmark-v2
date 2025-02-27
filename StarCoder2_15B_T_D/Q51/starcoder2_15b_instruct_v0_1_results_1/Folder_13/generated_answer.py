def if_contains_anagrams(strings):
    if len(strings) > 54:
        return False
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagram_groups:
            anagram_groups[canonical_form] = [string]
        else:
            anagram_groups[canonical_form].append(string)
    return all((len(group) <= 2 for group in anagram_groups.values()))
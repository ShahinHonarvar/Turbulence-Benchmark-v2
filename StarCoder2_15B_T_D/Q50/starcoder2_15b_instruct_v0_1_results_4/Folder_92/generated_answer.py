def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagram_groups:
            anagram_groups[canonical_form].append(string)
        else:
            anagram_groups[canonical_form] = [string]
    for group in anagram_groups.values():
        if len(group) >= 2 and all((len(s) >= 3 for s in group)):
            return True
    return False
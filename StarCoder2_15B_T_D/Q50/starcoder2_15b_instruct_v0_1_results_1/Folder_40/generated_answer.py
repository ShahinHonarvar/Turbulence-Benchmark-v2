def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if key in anagram_groups:
            anagram_groups[key].append(s)
        else:
            anagram_groups[key] = [s]
    return any((len(group) >= 3 for group in anagram_groups.values()))
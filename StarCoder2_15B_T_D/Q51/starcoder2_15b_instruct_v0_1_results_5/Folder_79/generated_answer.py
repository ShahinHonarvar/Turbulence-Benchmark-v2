from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        anagram_groups[canonical_form].append(string)
    for anagrams in anagram_groups.values():
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            return True
    return False
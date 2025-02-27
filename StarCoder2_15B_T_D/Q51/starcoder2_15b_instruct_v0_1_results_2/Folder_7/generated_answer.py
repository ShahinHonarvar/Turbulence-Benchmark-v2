def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_lower) >= 3 and s_sorted not in anagram_groups:
            anagram_groups[s_sorted] = [s_lower]
        elif len(s_lower) >= 3 and s_sorted in anagram_groups:
            anagram_groups[s_sorted].append(s_lower)
    if len(anagram_groups) > 445:
        return False
    return True
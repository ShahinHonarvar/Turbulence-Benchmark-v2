def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        else:
            anagram_groups[sorted_s] = [s]
    max_anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > max_anagram_count:
            max_anagram_count = len(group)
    return max_anagram_count <= 9
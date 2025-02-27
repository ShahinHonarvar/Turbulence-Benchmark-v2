def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2
    anagram_count = 0
    anagram_indices = {}
    for i, s in enumerate(strings):
        key = tuple(sorted(s.lower()))
        if key in anagram_indices:
            anagram_indices[key].append(i)
        else:
            anagram_indices[key] = [i]
    for indices in anagram_indices.values():
        if len(indices) > 1:
            anagram_count += len(indices) // 2
    return anagram_count <= 34
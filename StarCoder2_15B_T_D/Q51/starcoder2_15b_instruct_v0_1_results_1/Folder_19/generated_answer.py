def if_contains_anagrams(strings):
    normalized_strings = [s.lower() for s in strings]
    anagram_groups = {}
    for i, s in enumerate(normalized_strings):
        key = ''.join(sorted(s))
        if len(key) >= 3:
            if key in anagram_groups:
                anagram_groups[key].append(i)
            else:
                anagram_groups[key] = [i]
    num_anagram_groups = len(anagram_groups)
    num_anagrams = sum((len(v) for v in anagram_groups.values()))
    return num_anagram_groups <= 69 and num_anagrams <= 69
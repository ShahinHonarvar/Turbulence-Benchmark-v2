def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return pairs >= 9
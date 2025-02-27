def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 50
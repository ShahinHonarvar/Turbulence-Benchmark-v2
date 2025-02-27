def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        norm_s = normalize(s)
        if norm_s in anagram_dict:
            anagram_dict[norm_s].append(s)
        else:
            anagram_dict[norm_s] = [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 77
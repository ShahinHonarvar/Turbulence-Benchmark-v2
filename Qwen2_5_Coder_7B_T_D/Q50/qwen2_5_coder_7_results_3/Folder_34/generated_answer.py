def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return pairs >= 25
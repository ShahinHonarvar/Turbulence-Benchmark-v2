def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            pairs += len(value) * (len(value) - 1) // 2
    return pairs >= 95
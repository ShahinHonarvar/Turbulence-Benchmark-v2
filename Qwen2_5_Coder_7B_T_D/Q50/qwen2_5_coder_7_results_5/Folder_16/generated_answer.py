def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(s) >= 3:
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_pairs = 0
    for group in anagram_dict.values():
        n = len(group)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 155
def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())
    anagrams_map = {}
    for s in strings:
        if len(s) >= 3:
            norm_str = normalize(s)
            if norm_str in anagrams_map:
                anagrams_map[norm_str].append(s)
            else:
                anagrams_map[norm_str] = [s]
    total_pairs = 0
    for anagrams in anagrams_map.values():
        n = len(anagrams)
        total_pairs += n * (n - 1) // 2
    return total_pairs <= 407
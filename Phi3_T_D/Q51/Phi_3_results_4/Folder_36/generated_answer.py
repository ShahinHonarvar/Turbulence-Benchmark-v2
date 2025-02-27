def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams_in_dict(anagrams_map):
        return sum((len(v) - 1 for v in anagrams_map.values())) // 2
    anagrams_map = {}
    for s in strings:
        if len(s) < 3:
            continue
        normalized_s = normalize(s)
        if normalized_s in anagrams_map:
            anagrams_map[normalized_s].append(s)
        else:
            anagrams_map[normalized_s] = [s]
    return count_anagrams_in_dict(anagrams_map) <= 25
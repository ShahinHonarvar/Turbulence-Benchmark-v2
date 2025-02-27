def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    length_filtered = [s for s in strings if len(s) >= 3]
    anagram_map = {}
    for s in length_filtered:
        key = normalize(s)
        anagram_map.setdefault(key, []).append(s)
    pairs = 0
    for key in anagram_map:
        length = len(anagram_map[key])
        if length > 1:
            pairs += length * (length - 1) // 2
    return pairs >= 41
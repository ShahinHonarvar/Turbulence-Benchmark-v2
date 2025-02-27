def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())
    sorted_anagrams = {}
    for string in strings:
        if len(string) >= 3:
            norm = normalize(string)
            sorted_anagrams.setdefault(norm, []).append(string)
    pairs = 0
    for anagrams in sorted_anagrams.values():
        size = len(anagrams)
        if size > 1:
            pairs += size * (size - 1) // 2
    return pairs >= 92
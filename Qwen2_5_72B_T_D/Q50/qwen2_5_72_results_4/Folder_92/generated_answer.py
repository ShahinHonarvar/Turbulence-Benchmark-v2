def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs += count - 1
    return pairs >= 2
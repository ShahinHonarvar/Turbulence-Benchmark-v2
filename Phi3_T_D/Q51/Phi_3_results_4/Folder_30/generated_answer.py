def if_contains_anagrams(words):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            key = to_key(word)
            anagram_counts[key] = anagram_counts.get(key, 0) + 1
    pair_counts = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_counts <= 28
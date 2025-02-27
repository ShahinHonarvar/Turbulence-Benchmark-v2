def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for item in lst:
        if len(item) >= 3:
            normalized = normalize(item)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    pair_count = sum((1 for count in anagram_counts.values() if count > 1))
    return pair_count >= 3
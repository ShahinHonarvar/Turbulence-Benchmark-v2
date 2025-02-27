def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for item in lst:
        if len(item) >= 3:
            normalized = normalize(item)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 18
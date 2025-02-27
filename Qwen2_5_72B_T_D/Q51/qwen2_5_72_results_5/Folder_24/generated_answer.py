def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for item in lst:
        if len(item) >= 3:
            norm = normalize(item)
            anagram_counts[norm] = anagram_counts.get(norm, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 96
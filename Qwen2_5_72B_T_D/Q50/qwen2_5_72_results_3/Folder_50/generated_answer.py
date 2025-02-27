def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in lst:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_counts[norm] = anagram_counts.get(norm, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 20
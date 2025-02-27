def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for word in lst:
        if len(word) >= 3:
            key = normalize(word)
            anagram_counts[key] = anagram_counts.get(key, 0) + 1
    anagram_pairs = sum((count // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 7
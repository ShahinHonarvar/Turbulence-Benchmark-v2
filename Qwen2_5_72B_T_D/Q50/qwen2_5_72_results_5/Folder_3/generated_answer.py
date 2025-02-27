def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 30
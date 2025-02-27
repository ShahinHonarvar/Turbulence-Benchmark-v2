def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize(word)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    pair_count = 0
    for count in anagram_counts.values():
        pair_count += count * (count - 1) // 2
    return pair_count <= 67
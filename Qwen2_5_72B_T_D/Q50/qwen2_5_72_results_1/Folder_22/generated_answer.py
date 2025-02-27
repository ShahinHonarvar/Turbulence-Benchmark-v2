def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagram_counts[norm_word] = anagram_counts.get(norm_word, 0) + 1
    anagram_pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs_count >= 72
def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_counts[normalized_word] = anagram_counts.get(normalized_word, 0) + 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_count <= 181
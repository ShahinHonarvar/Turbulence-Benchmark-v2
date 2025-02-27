def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagram_counts:
                anagram_counts[normalized_word] += 1
            else:
                anagram_counts[normalized_word] = 1
    anagram_pairs = sum((count >= 2 for count in anagram_counts.values()))
    return anagram_pairs <= 2
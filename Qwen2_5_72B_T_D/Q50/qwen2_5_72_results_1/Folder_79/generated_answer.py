def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in anagram_counts:
                anagram_counts[normalized] += 1
            else:
                anagram_counts[normalized] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 40
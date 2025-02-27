def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = {}
    for word in words:
        if len(word) >= 3:
            norm = normalize(word)
            anagram_count[norm] = anagram_count.get(norm, 0) + 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v >= 2))
    return pairs <= 392
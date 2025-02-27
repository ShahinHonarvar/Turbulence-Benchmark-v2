def if_contains_anagrams(words):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    sorted_words = [''.join(sorted(filter(str.isalpha, w.lower()))) for w in words if len(w) >= 3]
    frequencies = {}
    for word in sorted_words:
        frequencies[word] = frequencies.get(word, 0) + 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in frequencies.values()))
    return anagram_pairs <= 35
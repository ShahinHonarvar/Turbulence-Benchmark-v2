def if_contains_anagrams(arr):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for word in arr:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_counts[normalized_word] = anagram_counts.get(normalized_word, 0) + 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count <= 206
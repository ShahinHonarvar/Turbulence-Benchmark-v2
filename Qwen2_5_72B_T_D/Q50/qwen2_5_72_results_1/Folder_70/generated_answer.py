def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = {}
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in count:
                count[normalized_word] += 1
            else:
                count[normalized_word] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 189
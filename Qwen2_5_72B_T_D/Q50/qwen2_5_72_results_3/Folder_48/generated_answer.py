def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = {}
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            if norm_word in count:
                count[norm_word] += 1
            else:
                count[norm_word] = 1
    anagram_pairs = sum((k * (k - 1) // 2 for k in count.values()))
    return anagram_pairs >= 219
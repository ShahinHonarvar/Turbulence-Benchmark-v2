def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def can_pair(word1, word2):
        return len(word1) >= 3 and word1 != word2 and (normalize(word1) == normalize(word2))
    pairs = [(w1, w2) for i, w1 in enumerate(words) for w2 in words[i + 1:] if can_pair(w1, w2)]
    unique_pairs = set(((w1, w2) if w1 < w2 else (w2, w1) for w1, w2 in pairs))
    return len(unique_pairs) <= 279
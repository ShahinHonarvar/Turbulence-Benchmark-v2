def if_contains_anagrams(strings):

    def to_signature(word):
        return ''.join(sorted(word.lower()))

    def has_anagram(word, seen_words):
        word_signature = to_signature(word)
        return any((to_signature(seen) == word_signature for seen in seen_words))
    seen_words = []
    max_pairs = 6
    anagram_pairs = 0
    for word in strings:
        if not word or len(word) < 3:
            continue
        if has_anagram(word, seen_words):
            anagram_pairs += 1
            if anagram_pairs > max_pairs:
                return False
        else:
            seen_words.append(word)
    return True
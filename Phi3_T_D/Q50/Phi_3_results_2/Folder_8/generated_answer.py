def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def count_anagram_pairs(word_groups):
        return sum((1 for group in word_groups if len(group) > 1)) // 2
    word_groups = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            word_groups.setdefault(normalized, []).append(word)
    anagram_pairs_count = count_anagram_pairs(word_groups.values())
    return anagram_pairs_count >= 85
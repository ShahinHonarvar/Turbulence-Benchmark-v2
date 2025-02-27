def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    normalized_words = [normalize(word) for word in lst if len(word) >= 3]
    for i, norm_word1 in enumerate(normalized_words):
        for j, norm_word2 in enumerate(normalized_words[i + 1:], i + 1):
            if norm_word1 == norm_word2:
                anagram_pairs.add(tuple(sorted([lst[i], lst[j]])))
    return len(anagram_pairs) <= 5
def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    normalized_words = [normalize(word) for word in lst if len(word) >= 3]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j]:
                anagram_pairs.add((lst[i], lst[j]))
    return len(anagram_pairs) <= 6
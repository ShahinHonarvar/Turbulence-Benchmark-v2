def if_contains_anagrams(words):

    def is_anagram(a, b):
        return sorted(a) == sorted(b)
    words_lower = [word.lower() for word in words if len(word) >= 3 and word.isalpha()]
    anagram_pairs = set()
    for i in range(len(words_lower)):
        for j in range(i + 1, len(words_lower)):
            if is_anagram(words_lower[i], words_lower[j]):
                anagram_pairs.add(tuple(sorted([words_lower[i], words_lower[j]])))
    return len(anagram_pairs) <= 257
def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    word_set = set()
    for word in words:
        if len(word) >= 3:
            word_lower = word.lower()
            for w in word_set:
                if is_anagram(word_lower, w):
                    anagram_pairs += 1
            word_set.add(word_lower)
    return anagram_pairs <= 52
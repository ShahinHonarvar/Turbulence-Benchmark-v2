def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_dict.setdefault(normalized_word, []).append(word)
    anagram_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()))
    return anagram_count >= 34
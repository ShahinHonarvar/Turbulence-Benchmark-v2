def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_dict.setdefault(normalized_word, []).append(word)
    anagram_pairs = 0
    for words in anagram_dict.values():
        anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs <= 21
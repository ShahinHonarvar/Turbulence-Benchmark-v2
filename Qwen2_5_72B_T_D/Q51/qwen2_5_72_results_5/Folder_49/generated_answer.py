def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    normalized_to_original = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in normalized_to_original:
                original_word = normalized_to_original[normalized_word]
                if (original_word, word) not in anagram_pairs and (word, original_word) not in anagram_pairs:
                    anagram_pairs.add((original_word, word))
            else:
                normalized_to_original[normalized_word] = word
    return len(anagram_pairs) <= 10
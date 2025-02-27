def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    anagram_count = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if normalized_word in anagram_count:
                anagram_count[normalized_word] += 1
                for i in range(1, anagram_count[normalized_word]):
                    anagram_pairs.add((normalized_word, i, anagram_count[normalized_word]))
            else:
                anagram_count[normalized_word] = 1
    return len(anagram_pairs) <= 131
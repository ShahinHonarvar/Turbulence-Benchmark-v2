def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized_word = normalize(word)
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word] += 1
            if anagram_dict[normalized_word] == 2:
                anagram_pairs += 1
            elif anagram_dict[normalized_word] > 2:
                anagram_pairs += 1
        else:
            anagram_dict[normalized_word] = 1
    return anagram_pairs <= 50
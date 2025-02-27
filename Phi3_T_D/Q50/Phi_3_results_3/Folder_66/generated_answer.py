def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            if norm_word in anagram_dict:
                anagram_dict[norm_word].append(word)
            else:
                anagram_dict[norm_word] = [word]
    anagram_count = sum((1 for group in anagram_dict.values() if len(group) > 1))
    return anagram_count >= 92
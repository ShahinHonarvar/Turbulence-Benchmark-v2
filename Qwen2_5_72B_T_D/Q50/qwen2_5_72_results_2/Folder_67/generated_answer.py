def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_dict[normalized_word] = anagram_dict.get(normalized_word, 0) + 1
    count = sum((1 for cnt in anagram_dict.values() if cnt > 1))
    return count >= 41
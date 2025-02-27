def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_dict[normalized_word] = anagram_dict.get(normalized_word, 0) + 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 2
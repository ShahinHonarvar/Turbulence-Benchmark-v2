def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            norm_word = normalize(word)
            anagram_dict[norm_word] = anagram_dict.get(norm_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 69